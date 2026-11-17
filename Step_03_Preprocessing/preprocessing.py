"""Shared deterministic English preprocessing for both retrieval engines.
AI-assisted revision of the supplied starter script; review before submission.
Boolean operators must be parsed separately before calling preprocess().
"""
import argparse
import csv
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer

_STEMMER = PorterStemmer()
# Keep negation terms: they can carry meaning in biomedical free-text search.
STOPWORDS = frozenset(ENGLISH_STOP_WORDS) - {'no', 'not', 'nor', 'never', 'without'}
TOKEN_PATTERN = re.compile(r"[a-z]+(?:'[a-z]+)?|\d+")


@lru_cache(maxsize=200000)
def _stem(term: str) -> str:
    return _STEMMER.stem(term)


def normalize_text(text: str) -> str:
    if text is None:
        return ''
    if not isinstance(text, str):
        raise TypeError('Text must be a string or None')
    return ' '.join(unicodedata.normalize('NFKC', text).replace('’', "'").lower().split())


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(normalize_text(text))


def preprocessing_steps(text: str, remove_stopwords: bool = True, stem: bool = True) -> dict:
    lowered = normalize_text(text)
    tokens = TOKEN_PATTERN.findall(lowered)
    filtered = [t for t in tokens if t not in STOPWORDS] if remove_stopwords else tokens.copy()
    final = [_stem(t) for t in filtered] if stem else filtered.copy()
    return {'original': text, 'normalized': lowered, 'tokens': tokens,
            'after_stopwords': filtered, 'final_terms': final,
            'remove_stopwords': remove_stopwords, 'stemming': stem}


def preprocess(text: str, remove_stopwords: bool = True, stem: bool = True) -> list[str]:
    """Preserve the original callable interface for downstream modules."""
    return preprocessing_steps(text, remove_stopwords, stem)['final_terms']


def normalized(text: str, remove_stopwords: bool = True, stem: bool = True) -> str:
    return ' '.join(preprocess(text, remove_stopwords, stem))


def document_text(record: dict) -> str:
    """Shared searchable field: title followed by body."""
    return f"{record.get('title') or ''} {record.get('text') or ''}".strip()


def self_test():
    assert tokenize('COVID-19 VACCINES') == ['covid', '19', 'vaccines']
    assert preprocess('The vaccines are effective', stem=False) == ['vaccines', 'effective']
    assert preprocess('The vaccines', False, False) == ['the', 'vaccines']
    assert preprocess('vaccines vaccinated vaccination') == ['vaccin'] * 3
    assert preprocess('not infected', stem=False) == ['not', 'infected']
    assert preprocess(None) == preprocess('  ') == preprocess('!!!') == []
    assert normalized('COVID-19') == 'covid 19'
    assert document_text({'title':'Title','text':'Body'}) == 'Title Body'
    print('PASS: synthetic fixture — tokenization, stopwords, stemming, negation, empty text, shared document fields')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--text', help='Demonstrate a supplied example')
    group.add_argument('--dataset', type=Path, help='Demonstrate the first real CSV document')
    group.add_argument('--self-test', action='store_true')
    parser.add_argument('--keep-stopwords', action='store_true')
    parser.add_argument('--no-stem', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        if args.dataset:
            with args.dataset.open(encoding='utf-8', newline='') as f:
                row = next(csv.DictReader(f), None)
            if not row or not all(row.get(k) for k in ('document_id','title','text')):
                parser.error('CSV must contain a valid document_id, title and text')
            text = document_text(row)
            print(f"Document ID: {row['document_id']}")
        else:
            text = args.text if args.text is not None else 'COVID-19 vaccines are reducing infections and improving immune responses.'
            print('User-provided or illustrative text (not dataset evidence)')
        print(json.dumps(preprocessing_steps(text, not args.keep_stopwords, not args.no_stem), ensure_ascii=False, indent=2))
