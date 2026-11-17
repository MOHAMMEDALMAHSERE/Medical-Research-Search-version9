"""Acquire a reproducible, cleaned TREC-COVID sample (Python 3.10+).
Source: https://huggingface.co/datasets/BeIR/trec-covid
AI-assisted revision of the supplied starter script; review before submission.
"""
import argparse
import csv
import gzip
import hashlib
import json
import random
import re
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path

DATASET = 'BeIR/trec-covid'
REVISION = 'e068f9faf522968e3cdbb275c466c51edcaf4d1a'
URL = f'https://huggingface.co/datasets/{DATASET}/resolve/{REVISION}/corpus.jsonl.gz'
SHA256 = '1bcbb294282f84a6c38d3881af2c7f392afcf88c1247e7599546cb33f33cb48c'
FIELDS = ['document_id', 'title', 'text', 'source']
OUT = Path(__file__).resolve().parent / 'dataset' / 'documents.csv'


def digest(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def compressed_records(path):
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def clean_and_sample(records, n, seed=42):
    """Uniform reservoir sampling over valid unique rows in source order."""
    if n < 1:
        raise ValueError('Sample size must be positive')
    ids, content, sample = set(), set(), []
    counts = Counter(examined=0, missing_fields=0, nonsearchable=0,
                     duplicate_id=0, duplicate_content=0, valid=0)
    rng = random.Random(seed)
    for record in records:
        counts['examined'] += 1
        raw = [record.get('_id', record.get('document_id')), record.get('title'), record.get('text')]
        if any(not isinstance(v, str) or not v.strip() for v in raw):
            counts['missing_fields'] += 1
            continue
        id_, title, body = (v.strip() for v in raw)
        if not re.search(r'[A-Za-z]{2,}', title) or not re.search(r'[A-Za-z]{2,}', body):
            counts['nonsearchable'] += 1
            continue
        key = hashlib.sha256(json.dumps([ ' '.join(title.casefold().split()),
                  ' '.join(body.casefold().split())], ensure_ascii=False).encode('utf-8')).digest()
        if id_ in ids:
            counts['duplicate_id'] += 1
            continue
        if key in content:
            counts['duplicate_content'] += 1
            continue
        ids.add(id_)
        content.add(key)
        counts['valid'] += 1
        row = dict(zip(FIELDS, (id_, title, body, DATASET)))
        if len(sample) < n:
            sample.append(row)
        else:
            j = rng.randrange(counts['valid'])
            if j < n:
                sample[j] = row
    if len(sample) < n:
        raise ValueError(f'Only {len(sample)} valid records; requested {n}')
    return sorted(sample, key=lambda r: r['document_id']), dict(counts)


def save_dataset(n=1000, out=OUT, seed=42, archive=None):
    if n < 100:
        raise ValueError('Phase 1 requires at least 100 documents')
    out = Path(out)
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(archive) if archive else Path(tmp) / 'corpus.jsonl.gz'
        if not archive:
            print(f'Downloading pinned corpus: {URL}', flush=True)
            request = urllib.request.Request(URL, headers={'User-Agent': 'MedicalResearchSearch/1.0'})
            with urllib.request.urlopen(request, timeout=120) as response, path.open('wb') as f:
                while chunk := response.read(1024 * 1024):
                    f.write(chunk)
        if digest(path) != SHA256:
            raise ValueError('Corpus checksum mismatch; use the exact pinned archive.')
        rows, counts = clean_and_sample(compressed_records(path), n, seed)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    report = dict(dataset=DATASET, revision=REVISION, source_url=URL,
                  archive_sha256=SHA256, method='reservoir sampling without replacement',
                  seed=seed, counts=counts, selected=len(rows), csv_sha256=digest(out),
                  selected_ids=[r['document_id'] for r in rows])
    report_path = out.parent / 'dataset_report.json'
    report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k != 'selected_ids'}, indent=2))
    print(f'Saved {len(rows)} documents to {out}\nReport: {report_path}')
    return report


def self_test():
    rows = [{'_id': str(i), 'title': f'Article {i}', 'text': f'Biomedical research {i}'} for i in range(20)]
    rows += [dict(rows[0]), dict(rows[1], _id='extra'), {'_id':None,'title':'Test','text':'Research'}, {'_id':'blank','title':'','text':'Research'}, {'_id':'bad','title':'123','text':'456'}]
    a, c = clean_and_sample(rows, 10)
    b, _ = clean_and_sample(rows, 10)
    assert a == b and len(a) == 10 and len({r['document_id'] for r in a}) == 10
    assert c == dict(examined=25, missing_fields=2, nonsearchable=1, duplicate_id=1, duplicate_content=1, valid=20), c
    assert len(clean_and_sample(rows, 20)[0]) == 20
    try:
        clean_and_sample(rows, 21)
    except ValueError:
        pass
    else:
        raise AssertionError('Insufficient corpus accepted')
    print('PASS: synthetic fixture — filtering, duplicates, sample size, reproducibility, insufficient data')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--count', type=int, default=1000)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--out', type=Path, default=OUT)
    parser.add_argument('--archive', type=Path, help='Local copy of the exact pinned gzip archive')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        save_dataset(args.count, args.out, args.seed, args.archive)
