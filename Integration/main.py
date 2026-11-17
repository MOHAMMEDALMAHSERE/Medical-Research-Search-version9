"""Unified Medical Research Search CLI. AI-assisted revision of original main.py."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for folder in ('Step_05_Ranked_Search', 'Step_04_Boolean_Search', 'Step_03_Preprocessing'):
    sys.path.insert(0, str(ROOT / folder))

from preprocessing import preprocessing_steps, normalized
from inverted_index import build_inverted_index, load_documents
from boolean_search import boolean_search
from ranked_search import RankedSearch

DEFAULT_CSV = ROOT / 'Step_03_Preprocessing' / 'dataset' / 'documents.csv'

class SearchSystem:
    def __init__(self, documents):
        self.documents = documents
        self.by_id = {d['document_id']: d for d in documents}
        self.all_ids = set(self.by_id)
        self.index = build_inverted_index(documents)
        self.ranker = RankedSearch(documents)

    def stats(self):
        print(f'Documents: {len(self.documents)} | Vocabulary: {len(self.index)} | Postings: {sum(map(len, self.index.values()))}')
        print(f'TF-IDF shape: {self.ranker.matrix.shape} | Nonzero weights: {self.ranker.matrix.nnz}')

    def boolean(self, query, limit=10):
        hits = boolean_search(query, self.index, self.all_ids)
        print(f'Query: {query}\nMatches: {len(hits)}')
        for doc_id in sorted(hits)[:limit]:
            print(f'  {doc_id}: {self.by_id[doc_id]["title"]}')
        if len(hits) > limit:
            print(f'  ... {len(hits)-limit} more')
        return hits

    def ranked(self, query, top_k=5):
        hits = self.ranker.search(query, top_k)
        print(f'Query: {query}\nProcessed query: {normalized(query)}')
        if not hits:
            print('No positive similarity results.')
        for rank, doc in enumerate(hits, 1):
            print(f'{rank}. {doc["document_id"]} | {doc["score"]:.6f} | {doc["title"]}')
        if hits:
            contributions = self.ranker.explain(query, hits[0]['document_id'])
            print('Top result contributions: ' + ', '.join(f'{x["term"]}={x["contribution"]:.6f}' for x in contributions))
        print('Scores represent lexical similarity, not clinical quality.')
        return hits

    def preprocessing(self, text):
        steps = preprocessing_steps(text)
        for key in ('original', 'normalized', 'tokens', 'after_stopwords', 'final_terms'):
            print(f'{key}: {steps[key]}')

    def demo(self):
        self.stats()
        print('\n=== Preprocessing (illustrative input) ===')
        self.preprocessing('COVID-19 vaccines are reducing infections.')
        print('\n=== Boolean retrieval ===')
        for query in ('covid AND vaccine', 'covid OR vaccine', 'NOT vaccine', 'covid AND NOT vaccine', '(covid OR virus) AND vaccine'):
            self.boolean(query, 5)
        print('\n=== Ranked retrieval ===')
        for query in ('covid vaccine immune response', 'respiratory infection treatment', 'coronavirus transmission prevention'):
            self.ranked(query)
        print('\nDemo completed successfully.')

    def interactive(self):
        self.stats()
        while True:
            print('\n1. Boolean search\n2. Ranked search\n3. Preprocessing demonstration\n4. System statistics\n5. Full demo\n0. Exit')
            try:
                choice = input('Choose: ').strip()
                if choice == '0':
                    return
                if choice == '1':
                    self.boolean(input('Boolean query: '))
                elif choice == '2':
                    query = input('Search query: ')
                    top_k = int(input('Top-K [5]: ').strip() or '5')
                    self.ranked(query, top_k)
                elif choice == '3':
                    self.preprocessing(input('Text: '))
                elif choice == '4':
                    self.stats()
                elif choice == '5':
                    self.demo()
                else:
                    print('Choose 0–5.')
            except ValueError as exc:
                print(f'Input error: {exc}')
            except (EOFError, KeyboardInterrupt):
                print('\nExiting.')
                return


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dataset', type=Path, default=DEFAULT_CSV)
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    try:
        print(f'Dataset: {args.dataset.name}')
        system = SearchSystem(load_documents(args.dataset))
        if args.demo:
            system.demo()
        else:
            system.interactive()
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Error: {exc}\nCheck the dataset path; generate the CSV with Step 03 if missing.\n')

if __name__ == '__main__':
    main()
