"""System and regression tests for the fixed 1,000-document Phase 1 corpus.
AI-assisted test implementation. Run with Python from any working directory.
"""
import contextlib
import io
import math
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'Integration'))
from main import SearchSystem, DEFAULT_CSV, load_documents
from preprocessing import preprocess, preprocessing_steps
from inverted_index import build_inverted_index, get_postings
from boolean_search import boolean_search
from ranked_search import RankedSearch


class SyntheticTests(unittest.TestCase):
    def setUp(self):
        self.docs = [
            dict(document_id='A', title='Vaccine', text='COVID vaccines prevent infection.'),
            dict(document_id='B', title='Virus', text='COVID virus transmission.'),
            dict(document_id='C', title='Influenza', text='Influenza vaccination.'),
            dict(document_id='D', title='The', text='and the'),
        ]
        self.system = SearchSystem(self.docs)

    def test_preprocessing(self):
        steps = preprocessing_steps('COVID-19 vaccines are reducing infections.')
        self.assertEqual(steps['tokens'], ['covid','19','vaccines','are','reducing','infections'])
        self.assertEqual(steps['final_terms'], ['covid','19','vaccin','reduc','infect'])
        self.assertEqual(preprocess('The vaccines', False, False), ['the','vaccines'])

    def test_index(self):
        self.assertEqual(get_postings(self.system.index, 'vaccines'), {'A','C'})
        self.assertEqual(get_postings(self.system.index, 'covid'), {'A','B'})
        self.assertEqual(get_postings(self.system.index, 'zzunknown'), set())
        with self.assertRaises(ValueError):
            build_inverted_index(self.docs + [self.docs[0]])

    def test_boolean_logic(self):
        cases = {'covid AND vaccine': {'A'}, 'covid OR vaccine': {'A','B','C'},
                 'NOT vaccine': {'B','D'}, 'covid AND NOT vaccine': {'B'},
                 'covid OR vaccine AND virus': {'A','B'},
                 '(covid OR vaccine) AND virus': {'B'}, 'NOT NOT covid': {'A','B'},
                 'zzunknown': set(), 'NOT zzunknown': {'A','B','C','D'}}
        for query, expected in cases.items():
            with self.subTest(query=query):
                self.assertEqual(boolean_search(query, self.system.index, self.system.all_ids), expected)

    def test_invalid_boolean(self):
        for query in ('', 'AND covid', 'covid OR', '(covid', 'covid)', '()'):
            with self.subTest(query=query), self.assertRaises(ValueError):
                self.system.boolean(query)

    def test_ranked_top_k_and_bounds(self):
        hits = self.system.ranker.search('covid vaccine', 10)
        self.assertEqual(hits[0]['document_id'], 'A')
        self.assertEqual(self.system.ranker.search('covid vaccine', 1), hits[:1])
        self.assertTrue(all(0 < h['score'] <= 1 + 1e-12 for h in hits))
        self.assertEqual([h['score'] for h in hits], sorted((h['score'] for h in hits), reverse=True))

    def test_ranked_empty_and_invalid(self):
        for query in ('', 'the and', 'zzunknown'):
            self.assertEqual(self.system.ranker.search(query), [])
        for k in (0, -1, True, 1.5):
            with self.subTest(k=k), self.assertRaises(ValueError):
                self.system.ranker.search('covid', k)
        for docs in ([], self.docs + [self.docs[0]]):
            with self.assertRaises(ValueError):
                RankedSearch(docs)

    def test_ranking_ties(self):
        docs = [dict(document_id=i, title='Vaccine', text='COVID vaccine') for i in ('B','A')]
        self.assertEqual([h['document_id'] for h in RankedSearch(docs).search('covid')], ['A','B'])

    def test_invalid_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'bad.csv'
            for content in ('wrong,columns\na,b\n', 'document_id,title,text\nA,title,\n',
                            'document_id,title,text\nA,title,text\nA,title,other\n'):
                path.write_text(content, encoding='utf-8')
                with self.assertRaises(ValueError):
                    load_documents(path)
            with self.assertRaises(OSError):
                load_documents(Path(directory) / 'missing.csv')

    def test_interactive_menu(self):
        output = io.StringIO()
        inputs = ['9','1','covid AND','1','covid AND vaccine','2','covid','0',
                  '2','covid vaccine','1','3','COVID vaccines','4','0']
        with patch('builtins.input', side_effect=inputs), contextlib.redirect_stdout(output):
            self.system.interactive()
        for text in ('Choose 0', 'Input error:', 'Matches: 1', 'Top result contributions:',
                     'final_terms:', 'Documents: 4'):
            self.assertIn(text, output.getvalue())


class RealCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = load_documents(DEFAULT_CSV)
        cls.system = SearchSystem(cls.docs)

    def test_dataset_integrity(self):
        self.assertEqual(len(self.docs), 1000)
        self.assertEqual(len(self.system.all_ids), 1000)
        self.assertTrue(all(all(d[k].strip() for k in ('document_id','title','text')) for d in self.docs))
        self.assertEqual(len({(' '.join(d['title'].casefold().split()), ' '.join(d['text'].casefold().split())) for d in self.docs}), 1000)

    def test_index_matrix_consistency(self):
        index = self.system.index
        ranker = self.system.ranker
        self.assertEqual(len(index), 10758)
        self.assertEqual(sum(map(len, index.values())), 87381)
        self.assertEqual(ranker.matrix.shape, (1000,10758))
        self.assertEqual(ranker.matrix.nnz, 87381)
        self.assertEqual(set(index), set(ranker.vectorizer.vocabulary_))
        for term, ids in index.items():
            column = ranker.vectorizer.vocabulary_[term]
            # Detailed equality is checked below using the CSC representation.
            self.assertTrue(ids <= self.system.all_ids)
        matrix = ranker.matrix.tocsc()
        for term, col in ranker.vectorizer.vocabulary_.items():
            rows = matrix.indices[matrix.indptr[col]:matrix.indptr[col+1]]
            self.assertEqual(index[term], {self.docs[i]['document_id'] for i in rows}, term)

    def test_boolean_regression(self):
        cases = {'covid AND vaccine':21, 'covid OR vaccine':357, 'NOT vaccine':923,
                 'covid AND NOT vaccine':280, '(covid OR virus) AND vaccine':53}
        for query, count in cases.items():
            with self.subTest(query=query), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(len(self.system.boolean(query)), count)

    def test_ranked_regression(self):
        cases = {
            'covid vaccine immune response': [('6fhuon6k',.451483),('1d17iafs',.396692),('od4c6fcg',.354211),('vbqgyll9',.335271),('0pmsfrcx',.320604)],
            'respiratory infection treatment': [('yqr3e4kp',.331911),('3hgupch5',.220218),('ckbik777',.210443),('r286hc2k',.206962),('vzwu2qol',.205862)],
            'coronavirus transmission prevention': [('nlzdto1h',.279990),('w0vm70no',.195235),('ynaum52m',.189076),('m1hampmt',.182151),('b0wd2jd3',.168638)]}
        ranker = self.system.ranker
        vocab = ranker.vectorizer.vocabulary_.copy()
        idf = ranker.vectorizer.idf_.copy()
        for query, expected in cases.items():
            with self.subTest(query=query), contextlib.redirect_stdout(io.StringIO()):
                hits = self.system.ranked(query, 5)
                self.assertEqual([h['document_id'] for h in hits], [i for i,s in expected])
                for hit, (_, score) in zip(hits, expected):
                    self.assertAlmostEqual(hit['score'], score, delta=0.000001)
                contributions = ranker.explain(query, hits[0]['document_id'])
                self.assertTrue(math.isclose(sum(t['contribution'] for t in contributions), hits[0]['score'], abs_tol=1e-12))
        self.assertEqual(vocab, ranker.vectorizer.vocabulary_)
        self.assertTrue((idf == ranker.vectorizer.idf_).all())

    def test_cli_demo_from_different_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT/'Integration'/'main.py'), '--demo'],
                                    cwd=directory, capture_output=True, encoding='utf-8', timeout=120)
        self.assertEqual(result.returncode, 0, result.stderr)
        for marker in ('Documents: 1000', 'Matches: 21', '0.451483', 'Demo completed successfully.'):
            self.assertIn(marker, result.stdout)

    def test_cli_missing_dataset(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, '-X', 'utf8', str(ROOT/'Integration'/'main.py'), '--dataset', str(Path(directory)/'missing.csv'), '--demo'], capture_output=True, encoding='utf-8', timeout=120)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Error:', result.stderr)


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    unittest.main(verbosity=2)
