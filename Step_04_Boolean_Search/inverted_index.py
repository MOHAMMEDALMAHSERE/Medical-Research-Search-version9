"""Dictionary/set inverted index. AI-assisted revision of supplied starter.
Requires the shared preprocessing.py from Step 03 (same directory or PYTHONPATH).
"""
import argparse
import csv
from pathlib import Path
from preprocessing import preprocess


def build_inverted_index(documents: list[dict]) -> dict[str, set[str]]:
    """Index title + text using each document's unique string ID."""
    index, seen = {}, set()
    for doc in documents:
        doc_id = doc['document_id']
        if not isinstance(doc_id, str) or not doc_id.strip() or doc_id in seen:
            raise ValueError(f'Invalid or duplicate document ID: {doc_id!r}')
        seen.add(doc_id)
        for term in set(preprocess(doc['title'] + ' ' + doc['text'])):
            index.setdefault(term, set()).add(doc_id)
    return index


def document_lookup(documents):
    return {doc['document_id']: doc for doc in documents}


def get_postings(index, query_term):
    """Look up a single normalized term without exposing mutable index sets."""
    terms = preprocess(query_term)
    if not terms:
        return set()
    if len(terms) != 1:
        raise ValueError('Posting lookup requires exactly one processed term')
    return set(index.get(terms[0], set()))


def load_documents(path):
    """Load a prepared CSV; reject invalid IDs, titles and text."""
    with Path(path).open(encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        if not {'document_id', 'title', 'text'}.issubset(reader.fieldnames or []):
            raise ValueError('CSV must contain document_id, title, text')
        docs, ids = [], set()
        for row in reader:
            doc = {k: (row[k] or '').strip() for k in ('document_id', 'title', 'text')}
            if not all(doc.values()) or doc['document_id'] in ids:
                raise ValueError(f'Invalid row or duplicate ID: {doc["document_id"]!r}')
            ids.add(doc['document_id'])
            docs.append(doc)
    if not docs:
        raise ValueError('Empty document collection')
    return docs


def fixture_documents():
    """Synthetic data for tests only, not real corpus evidence."""
    return [
        {'document_id': 'D1', 'title': 'Vaccine', 'text': 'COVID vaccines prevent infection.'},
        {'document_id': 'D2', 'title': 'Virus', 'text': 'COVID virus transmission.'},
        {'document_id': 'D3', 'title': 'Influenza', 'text': 'Influenza vaccination.'},
        {'document_id': 'D4', 'title': 'The', 'text': 'and the'},
    ]


def self_test():
    docs = fixture_documents()
    index = build_inverted_index(docs)
    assert get_postings(index, 'vaccines') == {'D1', 'D3'}
    assert get_postings(index, 'covid') == {'D1', 'D2'}
    assert get_postings(index, 'zzunknown') == set()
    assert all(isinstance(v, set) for v in index.values())
    assert set(document_lookup(docs)) == {'D1', 'D2', 'D3', 'D4'}
    assert 'D4' not in set().union(*index.values())
    copy = get_postings(index, 'covid'); copy.clear()
    assert get_postings(index, 'covid') == {'D1', 'D2'}
    assert build_inverted_index([]) == {}
    try:
        build_inverted_index(docs + [docs[0]])
    except ValueError:
        pass
    else:
        raise AssertionError('Duplicate ID accepted')
    print('PASS: synthetic fixture — posting lists, stemming, unknown terms, sets, complete IDs, empty index, duplicate ID rejection, defensive copy')


def demo(docs, terms, limit):
    index = build_inverted_index(docs)
    by_id = document_lookup(docs)
    print(f'Documents: {len(by_id)}; unique terms: {len(index)}; postings: {sum(map(len, index.values()))}')
    print(f'Documents with zero indexed terms: {len(set(by_id) - set().union(*index.values()))}')
    for query in terms:
        matches = sorted(get_postings(index, query))
        print(f'\nTerm: {query}; document frequency: {len(matches)}; sample IDs: {matches[:limit]}')
        for doc_id in matches[:limit]:
            print(f'  {doc_id}: {by_id[doc_id]["title"]}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test', action='store_true')
    group.add_argument('--dataset', type=Path)
    parser.add_argument('--terms', nargs='+', default=['covid', 'vaccine', 'virus'])
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    if args.self_test:
        self_test()
    else:
        print(f'Input CSV: {args.dataset}')
        demo(load_documents(args.dataset), args.terms, args.limit)
