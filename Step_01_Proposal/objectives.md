# Project Objectives

## 1. General Objective

Develop a functional Python-based Information Retrieval System that enables users to search and retrieve relevant biomedical research articles using Boolean retrieval and relevance-based ranked retrieval techniques.

## 2. Specific Objectives

### Objective 1 — Dataset Preparation

- Acquire a real biomedical research dataset from TREC-COVID (BEIR).
- Prepare a reproducible collection targeting 1,000 unique English documents.
- Remove duplicate, missing, and empty records.
- Assign unique document IDs and maintain document titles and text.

### Objective 2 — Text Preprocessing

- Implement text normalization and lowercasing.
- Apply tokenization.
- Implement configurable stopword handling.
- Apply stemming or lemmatization.
- Ensure consistent preprocessing of documents and user queries.

### Objective 3 — Inverted Index Construction

- Construct an inverted index using Python dictionaries and sets.
- Generate posting lists for indexed terms.
- Associate each term with the corresponding document IDs.
- Enable efficient term-based document retrieval.

### Objective 4 — Boolean Information Retrieval

- Implement AND, OR, and NOT operators.
- Retrieve documents that exactly match Boolean query conditions.
- Display matching document IDs and titles.
- Demonstrate at least one successful query for each Boolean operator.

### Objective 5 — Ranked Information Retrieval

- Represent documents using TF-IDF vectors.
- Transform user queries using the previously fitted vectorizer.
- Calculate cosine similarity between queries and documents.
- Rank documents in descending order of similarity.
- Return Top-K results with document IDs, titles, and similarity scores.
- Demonstrate at least three ranked search queries.

### Objective 6 — System Integration and Validation

- Integrate all implemented modules into a unified search engine.
- Provide a functional Python console interface.
- Ensure both retrieval approaches use the same document collection.
- Handle empty and invalid queries.
- Verify system functionality through reproducible tests.
- Document individual contributions and implementation results.

## 3. Success Criteria

| Component | Expected Result |
|---|---|
| Dataset | At least 100 unique, valid documents, with a target of 1,000 |
| Text Preprocessing | Functional preprocessing pipeline with before-and-after examples |
| Inverted Index | Correct term-to-document mapping |
| Boolean Search | Working AND, OR, and NOT operations |
| Ranked Search | Correct TF-IDF and cosine similarity ranking |
| Demonstration | At least three ranked queries and one test for each Boolean operator |
| Integration | Fully functional Python console application |
| Reproducibility | Documented execution commands and reproducible results |

## 4. Expected Outcome

By the end of Phase 1, the project aims to deliver an integrated and functional biomedical search engine that demonstrates the fundamental concepts of Information Retrieval, including text preprocessing, inverted indexing, Boolean retrieval, TF-IDF representation, and cosine similarity ranking.
