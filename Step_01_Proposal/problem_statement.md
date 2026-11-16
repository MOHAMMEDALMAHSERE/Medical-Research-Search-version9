# Problem Statement

## Project Title
Medical Research Search — A Python-Based Information Retrieval System

## 1. Background

Biomedical research produces a large number of scientific articles covering diseases, treatments, medications, vaccines, and medical discoveries. Finding relevant information within these articles can be challenging, especially when researchers need to examine multiple documents to identify useful evidence.

Information Retrieval (IR) systems help users search document collections and retrieve information relevant to their queries.

## 2. Problem Definition

Searching through a large collection of biomedical research articles manually is time-consuming and inefficient.

Users need a system that can identify documents containing specific medical terms and rank relevant articles according to their similarity to a search query.

This project addresses the problem by developing a Python-based Information Retrieval System using two complementary retrieval approaches:

- **Boolean Retrieval:** Retrieves documents matching exact logical conditions using AND, OR, and NOT operators.
- **Ranked Retrieval:** Uses TF-IDF and Cosine Similarity to rank documents based on their relevance to a user's query.

## 3. Target Users

The proposed system is intended for:

1. **Medical Researchers:** Searching for biomedical studies related to specific research topics.
2. **University Students:** Finding scientific articles for academic assignments and research.
3. **Healthcare Professionals:** Locating relevant biomedical publications for educational and research purposes.

## 4. Proposed Solution

The system will use a documented sample of biomedical research articles from the TREC-COVID (BEIR) dataset.

It will clean and preprocess text, construct an inverted index, support Boolean queries, and implement TF-IDF-based document ranking using Cosine Similarity.

Users will interact with the system through a Python console interface.

The system is designed for academic information retrieval and does not provide medical diagnoses or treatment recommendations.

## 5. Expected Outcome

The expected outcome is a working, reproducible Information Retrieval System that:

- Searches a real biomedical document collection.
- Supports Boolean search operations.
- Returns ranked search results with similarity scores.
- Displays document identifiers and titles.
- Demonstrates text preprocessing and indexing techniques.
- Integrates all retrieval modules into one functional Python application.
