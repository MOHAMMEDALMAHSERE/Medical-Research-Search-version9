"""TF-IDF and cosine ranked retrieval. AI-assisted revision of supplied starter.
Requires the shared Step 03 preprocessing module. No query-time model fitting.
"""
import argparse
import csv
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocessing import normalized

DEFAULT_CSV = Path(__file__).resolve().parent.parent / 'Step_03_Preprocessing' / 'dataset' / 'documents.csv'
QUERIES = ('covid vaccine immune response', 'respiratory infection treatment',
           'coronavirus transmission prevention')


class RankedSearch:
    def __init__(self, documents: list[dict]):
        self.documents = [dict(doc) for doc in documents]
        ids = set()
        texts = []
        for doc in self.documents:
            doc_id = doc['document_id']
            if not isinstance(doc_id, str) or not doc_id.strip() or doc_id in ids:
                raise ValueError(f'Invalid or duplicate document ID: {doc_id!r}')
            ids.add(doc_id)
            texts.append(normalized(doc['title'] + ' ' + doc['text']))
        if not any(texts):
            raise ValueError('No valid content to vectorize')
        self.vectorizer = TfidfVectorizer(lowercase=False, tokenizer=str.split,
                                          preprocessor=None, token_pattern=None,
                                          norm='l2', use_idf=True, smooth_idf=True,
                                          sublinear_tf=False)
        self.matrix = self.vectorizer.fit_transform(texts).tocsr()
        self._features = self.vectorizer.get_feature_names_out()
        self._rows = {doc['document_id']: i for i, doc in enumerate(self.documents)}

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Return positive-scoring results, ordered by score then document ID."""
        if isinstance(top_k, bool) or not isinstance(top_k, int) or top_k <= 0:
            raise ValueError('top_k must be a positive integer')
        vector = self.vectorizer.transform([normalized(query)])
        if vector.nnz == 0:
            return []
        similarities = cosine_similarity(vector, self.matrix).ravel()
        ranked = sorted((i for i, s in enumerate(similarities) if s > 0),
                        key=lambda i: (-similarities[i], self.documents[i]['document_id']))
        return [{**self.documents[i], 'score': float(similarities[i])}
                for i in ranked[:top_k]]

    def explain(self, query: str, document_id: str) -> list[dict]:
        """Shared term contributions to cosine (L2-normalized TF-IDF dot product)."""
        vector = self.vectorizer.transform([normalized(query)])
        row = self.matrix[self._rows[document_id]]
        products = vector.multiply(row).tocoo()
        return sorted(({'term': str(self._features[j]), 'contribution': float(v)}
                       for j, v in zip(products.col, products.data) if v > 0),
                      key=lambda item: (-item['contribution'], item['term']))


def load_documents(path: Path) -> list[dict]:
    with path.open(encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        if not {'document_id', 'title', 'text'}.issubset(reader.fieldnames or []):
            raise ValueError('CSV must contain document_id,title,text')
        docs = []
        for row in reader:
            doc = {key: (row[key] or '').strip() for key in ('document_id', 'title', 'text')}
            if not all(doc.values()):
                raise ValueError('CSV contains missing ID, title or text')
            docs.append(doc)
    return docs


def self_test():
    import math
    docs = [
        {'document_id': 'D1', 'title': 'Vaccine', 'text': 'COVID vaccine immune response'},
        {'document_id': 'D2', 'title': 'Virus', 'text': 'COVID virus transmission'},
        {'document_id': 'D3', 'title': 'Respiratory infection', 'text': 'Respiratory infection treatment'},
        {'document_id': 'D4', 'title': 'Vaccine', 'text': 'COVID vaccine immune response'},
    ]
    ranker = RankedSearch(docs)
    vocab = ranker.vectorizer.vocabulary_.copy()
    idf = ranker.vectorizer.idf_.copy()
    hits = ranker.search('COVID vaccines immune response', 10)
    assert [d['document_id'] for d in hits] == ['D1', 'D4', 'D2']
    assert all(0 < d['score'] <= 1 + 1e-12 for d in hits)
    assert all(a['score'] >= b['score'] for a, b in zip(hits, hits[1:]))
    assert ranker.search('COVID vaccines immune response', 1) == hits[:1]
    assert ranker.search('zzunknown') == ranker.search('') == ranker.search('the and') == []
    assert ranker.search('respiratory infection treatment')[0]['document_id'] == 'D3'
    assert math.isclose(sum(t['contribution'] for t in ranker.explain('COVID vaccines immune response', 'D1')), hits[0]['score'], abs_tol=1e-12)
    assert ranker.vectorizer.vocabulary_ == vocab and (ranker.vectorizer.idf_ == idf).all()
    assert ranker.matrix.shape == (4, len(vocab))
    for bad in (0, -1, 1.5, True):
        try:
            ranker.search('covid', bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid top_k accepted')
    for bad_docs in ([], docs + [docs[0]]):
        try:
            RankedSearch(bad_docs)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid corpus accepted')
    print('PASS: synthetic fixture — ranking, ties, score bounds, top-k, empty/OOV queries, term contributions, unchanged vocabulary/IDF, sparse matrix, invalid inputs')


def demo(documents, queries, top_k):
    ranker = RankedSearch(documents)
    print(f'Documents: {len(documents)} | Vocabulary: {ranker.matrix.shape[1]} | Nonzero weights: {ranker.matrix.nnz}')
    for query in queries:
        print(f'\nQuery: {query}\nProcessed query: {normalized(query)}')
        hits = ranker.search(query, top_k)
        if not hits:
            print('No positive similarity results.')
            continue
        for rank, doc in enumerate(hits, 1):
            print(f"{rank}. {doc['document_id']} | {doc['score']:.6f} | {doc['title']}")
        contributions = ranker.explain(query, hits[0]['document_id'])
        print('Top result explanation: highest cosine score in this collection; shared stem contributions:')
        print(', '.join(f"{item['term']}={item['contribution']:.6f}" for item in contributions))
        print('This is lexical relevance, not a clinical quality judgment.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=DEFAULT_CSV)
    parser.add_argument('--query', action='append', help='Repeat for multiple custom queries')
    parser.add_argument('--top-k', type=int, default=5)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        if args.top_k <= 0:
            parser.error('--top-k must be positive')
        demo(load_documents(args.dataset), args.query or QUERIES, args.top_k)
