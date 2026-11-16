# Expected Search Features

## 1. System Overview

The Medical Research Search system will provide a Python-based search engine for retrieving biomedical research documents from the TREC-COVID dataset.

The system will support two primary retrieval methods:

- Boolean Information Retrieval.
- Ranked Information Retrieval.

Both methods will operate on the same cleaned document collection.

## 2. Boolean Search

### Description

Boolean search allows users to retrieve documents that satisfy specific logical conditions using an inverted index.

### Supported Operators

| Operator | Operation | Description |
|---|---|---|
| AND | Intersection | Retrieves documents containing both terms |
| OR | Union | Retrieves documents containing either or both terms |
| NOT | Complement | Excludes documents containing the specified term |

### Input

A textual query containing search terms and Boolean operators.

### Example Queries

- covid AND vaccine
- coronavirus OR influenza
- vaccine AND NOT infection

### Processing

1. Parse the Boolean query.
2. Separate search terms from Boolean operators.
3. Apply text preprocessing to search terms.
4. Retrieve posting lists from the inverted index.
5. Apply the corresponding set operations.
6. Retrieve matching document information.

### Expected Output

- Original search query.
- Number of matching documents.
- Document IDs.
- Document titles.

## 3. Ranked Search

### Description

Ranked search retrieves and orders documents according to their relevance to a user query using TF-IDF and cosine similarity.

### Input

- A natural-language or keyword-based search query.
- The requested number of results (Top-K).

### Example Queries

- COVID vaccine immune response
- coronavirus transmission prevention
- antiviral treatment clinical trials

### Processing

1. Apply consistent text preprocessing to the document collection.
2. Fit the TF-IDF vectorizer on the document collection.
3. Generate document TF-IDF vectors.
4. Preprocess the user query.
5. Transform the query using the previously fitted vectorizer.
6. Calculate cosine similarity between the query and documents.
7. Sort documents by similarity score in descending order.
8. Return the Top-K relevant results.

### Expected Output

- Original search query.
- Document rank.
- Document ID.
- Document title.
- Cosine similarity score.

## 4. Text Preprocessing Features

The system will provide a configurable preprocessing pipeline supporting:

- Text normalization.
- Lowercasing.
- Tokenization.
- Stopword handling.
- Stemming or lemmatization.
- Consistent processing of documents and queries.
- Before-and-after preprocessing demonstrations.

Boolean operators will be preserved during query parsing and will not be removed as stopwords.

## 5. Additional System Features

- Dataset information display.
- Inverted index demonstration.
- Preprocessing demonstration.
- Configurable Top-K results.
- Empty query handling.
- Invalid query handling.
- Unknown search term handling.
- No-result handling.
- Reproducible search results.

## 6. User Interface

The system will provide a Python console interface with the following options:

1. Boolean Search
2. Ranked Search
3. Preprocessing Demonstration
4. Inverted Index Demonstration
5. Dataset Information
0. Exit

A graphical user interface is not required for Phase 1.

## 7. Retrieval Methods Comparison

| Feature | Boolean Search | Ranked Search |
|---|---|---|
| Retrieval Model | Boolean Model | Vector Space Model |
| Representation | Inverted Index | TF-IDF Vectors |
| Matching | Exact logical matching | Similarity-based matching |
| Query Type | Logical expressions | Keywords or natural language |
| Core Operations | AND, OR, NOT | Cosine Similarity |
| Result Ordering | No relevance-based ranking | Descending similarity score |
| Similarity Score | Not applicable | Available |
| Output | Matching document set | Ranked Top-K documents |

## 8. Phase 1 Limitations

The initial implementation will focus on traditional Information Retrieval techniques.

The following advanced features are outside the current Phase 1 scope:

- Semantic search.
- Query expansion.
- Spell correction.
- Relevance feedback.
- Formal retrieval evaluation metrics.
- Graphical and web-based interfaces.

## 9. Expected Outcome

The system is expected to provide functional, reproducible, and integrated Boolean and ranked retrieval capabilities for biomedical research documents.

All displayed search results must be generated dynamically from the indexed document collection rather than being hard-coded.
