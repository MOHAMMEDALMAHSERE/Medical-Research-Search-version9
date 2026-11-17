"""Boolean retrieval: NOT > AND > OR; parentheses; case-insensitive operators.
AI-assisted revision of the supplied starter. Uses shared Step 03 preprocessing.
Implicit AND between adjacent operands/groups; punctuation-expanded terms form
an AND group, so NOT COVID-19 negates the full group. NOT uses all document IDs.
"""
import argparse
import re
from pathlib import Path
from preprocessing import preprocess

OPERATORS = {'AND', 'OR', 'NOT'}
PRECEDENCE = {'OR': 1, 'AND': 2, 'NOT': 3}


def _tokenize(query):
    if not isinstance(query, str) or not query.strip():
        raise ValueError('Empty Boolean query')
    result = []
    for raw in re.findall(r'\(|\)|[^\s()]+', query):
        upper = raw.upper()
        if upper in OPERATORS or raw in ('(', ')'):
            parts = [upper]
        else:
            if '"' in raw or '=' in raw or '&' in raw or '|' in raw:
                raise ValueError('Use AND, OR, NOT and parentheses; phrases are not supported')
            terms = preprocess(raw)
            if not terms:
                raise ValueError(f'No searchable term in: {raw!r}')
            parts = terms[:1]
            for term in terms[1:]:
                parts.extend(['AND', term])
            if len(terms) > 1:
                parts = ['('] + parts + [')']
        previous_operand = result and result[-1] not in OPERATORS | {'('}
        next_operand = parts[0] not in {'AND', 'OR', ')'}
        if previous_operand and next_operand:
            result.append('AND')
        result.extend(parts)
    return result


def boolean_search(query: str, index: dict[str, set[str]], all_ids: set[str]) -> set[str]:
    """Validate syntax, convert to postfix, and evaluate using set operations."""
    tokens = _tokenize(query)
    output, ops = [], []
    expect_operand = True
    for token in tokens:
        if token == '(':
            if not expect_operand:
                raise ValueError('Missing operator before parenthesis')
            ops.append(token)
        elif token == ')':
            if expect_operand:
                raise ValueError('Missing operand before closing parenthesis')
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            if not ops:
                raise ValueError('Unmatched closing parenthesis')
            ops.pop()
            expect_operand = False
        elif token in OPERATORS:
            if token == 'NOT':
                if not expect_operand:
                    raise ValueError('NOT must precede an operand')
            elif expect_operand:
                raise ValueError(f'{token} requires a left operand')
            while (ops and ops[-1] in OPERATORS and
                   (PRECEDENCE[ops[-1]] > PRECEDENCE[token] or
                    (PRECEDENCE[ops[-1]] == PRECEDENCE[token] and token != 'NOT'))):
                output.append(ops.pop())
            ops.append(token)
            expect_operand = True
        else:
            if not expect_operand:
                raise ValueError('Missing operator between terms')
            output.append(token)
            expect_operand = False
    if expect_operand:
        raise ValueError('Query ends without an operand')
    while ops:
        op = ops.pop()
        if op == '(':
            raise ValueError('Unmatched opening parenthesis')
        output.append(op)
    stack = []
    for token in output:
        if token == 'NOT':
            stack.append(all_ids - stack.pop())
        elif token in ('AND', 'OR'):
            right, left = stack.pop(), stack.pop()
            stack.append(left & right if token == 'AND' else left | right)
        else:
            stack.append(set(index.get(token, set())) & all_ids)
    if len(stack) != 1:
        raise ValueError('Malformed Boolean query')
    return stack[0]


def self_test():
    # Standalone synthetic postings, not real corpus evidence.
    index = {'covid': {'D1', 'D2'}, 'vaccin': {'D1', 'D3'}, preprocess('virus')[0]: {'D2'}, '19': {'D1'}}
    ids = {'D1', 'D2', 'D3', 'D4'}
    cases = {
        'covid AND vaccine': {'D1'}, 'covid OR vaccine': {'D1', 'D2', 'D3'},
        'NOT vaccine': {'D2', 'D4'}, 'covid AND NOT vaccine': {'D2'},
        'covid OR vaccine AND virus': {'D1', 'D2'},
        '(covid OR vaccine) AND virus': {'D2'}, 'NOT NOT covid': {'D1', 'D2'},
        'NOT (covid OR vaccine)': {'D4'}, 'covid vaccine': {'D1'},
        '(covid OR virus) vaccine': {'D1'}, 'covid not vaccine': {'D2'},
        'NOT COVID-19': {'D2', 'D3', 'D4'}, 'CoViD aNd Vaccines': {'D1'},
        'zzunknown': set(), 'NOT zzunknown': ids,
    }
    for query, expected in cases.items():
        actual = boolean_search(query, index, ids)
        assert actual == expected, (query, actual, expected)
        print(f'PASS: {query} -> {sorted(actual)}')
    invalid = ['', 'AND covid', 'covid OR', 'covid AND OR virus', '()', '(covid', 'covid)', 'NOT', 'the', 'covid AND (virus OR)', 'covid AND ()', 'covid AND AND virus', 'covid = virus']
    for query in invalid:
        try:
            boolean_search(query, index, ids)
        except ValueError:
            continue
        raise AssertionError(f'Invalid query accepted: {query!r}')
    print(f'PASS: {len(cases)} valid + {len(invalid)} invalid queries on synthetic postings')


def demo(path, queries, limit):
    from inverted_index import build_inverted_index, load_documents, document_lookup
    documents = load_documents(path)
    index = build_inverted_index(documents)
    by_id = document_lookup(documents)
    print(f'Input CSV: {path}; indexed documents: {len(by_id)}')
    for query in queries:
        print(f'\nQuery: {query}')
        try:
            matches = sorted(boolean_search(query, index, set(by_id)))
            print(f'Matches: {len(matches)}')
            for doc_id in matches[:limit]:
                print(f'  {doc_id}: {by_id[doc_id]["title"]}')
            if len(matches) > limit:
                print(f'  ... {len(matches)-limit} more')
        except ValueError as error:
            print(f'Query error: {error}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test', action='store_true')
    group.add_argument('--dataset', type=Path)
    parser.add_argument('--query', action='append', help='Repeat for multiple queries')
    parser.add_argument('--limit', type=int, default=10)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    if args.self_test:
        self_test()
    else:
        demo(args.dataset, args.query or ['covid AND vaccine', 'covid OR vaccine', 'covid AND NOT vaccine', 'NOT vaccine', '(covid OR virus) AND vaccine'], args.limit)
