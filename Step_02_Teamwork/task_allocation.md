# Task Allocation and Module Ownership

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Students |

## 2. Task Allocation Overview

| Team Member | Assigned Module | Development Section | Priority | Status |
|---|---|---|---|---|
| Mohammed — Team Leader | Ranked Search and Integration | Step 05 / Integration | High | Planned |
| Mashhour Rami | Dataset Engineering | Step 03 | High | Planned |
| Omar Atiyeh | NLP and Text Preprocessing | Step 03 | High | Planned |
| Laith Jaber | Inverted Index | Step 04 | High | Planned |
| Mohammad Saleh | Boolean Search | Step 04 | High | Planned |

## 3. Individual Technical Tasks

### Task 01 — Dataset Acquisition and Cleaning

**Assigned to:** Mashhour Rami

**Branch:** `mashhour-rami`

**Directory:** `Step_03_Preprocessing/`

**Responsibilities:**

- Download the TREC-COVID corpus.
- Validate the original dataset structure.
- Remove duplicate documents.
- Remove missing and empty records.
- Select 1,000 valid documents using reproducible random sampling.
- Preserve unique document identifiers.
- Export the prepared dataset as CSV.
- Document dataset statistics.

**Expected Files:**

- `download_dataset.py`
- `data_cleaning.py`
- `dataset/documents.csv` (generated locally)
- `dataset_report.md`

**Input:** Original TREC-COVID corpus.

**Output:** Clean and structured document collection.

**Acceptance Criteria:**

- Target of 1,000 valid documents, with a minimum of 100.
- Unique document IDs.
- Non-empty titles and text.
- No exact duplicate documents.
- Reproducible sampling using random seed 42 and a fixed dataset revision.
- Documented dataset source and cleaning results.
- Raw documents must not be publicly redistributed unless permitted by applicable licenses.

### Task 02 — NLP and Text Preprocessing

**Assigned to:** Omar Atiyeh

**Branch:** `omar-atiyeh`

**Directory:** `Step_03_Preprocessing/`

**Responsibilities:**

- Implement text normalization.
- Convert text to lowercase.
- Implement tokenization.
- Implement configurable stopword handling.
- Apply stemming or lemmatization.
- Ensure consistent document and query preprocessing.
- Demonstrate preprocessing results.

**Expected Files:**

- `preprocessing.py`
- `preprocessing_demo.py`
- `preprocessing_report.md`

**Input:** Document text or user query terms.

**Output:** Processed list of searchable terms.

**Acceptance Criteria:**

- Functional and reusable preprocessing pipeline.
- Configurable stopword handling.
- Consistent processing of documents and queries.
- Safe handling of empty text.
- At least one original text, tokenization, and final processed terms demonstration.

### Task 03 — Inverted Index Construction

**Assigned to:** Laith Jaber

**Branch:** `laith-jaber`

**Directory:** `Step_04_Boolean_Search/`

**Responsibilities:**

- Construct the inverted index.
- Use Python dictionaries and sets.
- Generate posting lists.
- Map processed terms to document identifiers.
- Maintain the complete indexed document ID set.
- Support document title and metadata retrieval.
- Validate index construction.

**Expected Files:**

- `inverted_index.py`
- `index_demo.py`
- `index_report.md`

**Input:** Preprocessed documents and their identifiers.

**Output:** Inverted index and posting lists.

**Acceptance Criteria:**

- Correct term-to-document mapping.
- Posting lists implemented using Python sets.
- No duplicate document identifiers in posting lists.
- Support for unknown terms.
- Correct tracking of all indexed document IDs.
- Demonstration of actual posting lists.

### Task 04 — Boolean Search Engine

**Assigned to:** Mohammad Saleh

**Branch:** `mohammad-saleh`

**Directory:** `Step_04_Boolean_Search/`

**Responsibilities:**

- Implement Boolean query parsing.
- Implement AND using set intersection.
- Implement OR using set union.
- Implement NOT using set complement.
- Preserve Boolean operators during query parsing.
- Retrieve matching documents.
- Handle invalid and empty queries.
- Test supported Boolean operations.

**Expected Files:**

- `boolean_search.py`
- `boolean_demo.py`
- `boolean_report.md`

**Input:** Boolean query and inverted index.

**Output:** Matching document IDs and titles.

**Acceptance Criteria:**

- Correct AND, OR, and NOT operations.
- NOT must operate against the complete indexed document set.
- At least one successful test for each operator.
- Correct document IDs and titles.
- No hard-coded search results.

### Task 05 — Ranked Search Engine and System Integration

**Assigned to:** Mohammed — Team Leader

**Directory:** `Step_05_Ranked_Search/` and `Integration/`

**Responsibilities:**

- Design the overall system architecture.
- Implement TF-IDF document vectorization.
- Fit the vectorizer on the document collection.
- Transform user queries using the fitted vectorizer.
- Compute cosine similarity scores.
- Implement descending document ranking.
- Return Top-K search results.
- Develop the main console application.
- Integrate all project modules.
- Manage code reviews and pull requests.
- Coordinate team progress and final delivery.

**Expected Files:**

- `ranked_search.py`
- `ranking_demo.py`
- `ranking_report.md`
- `main.py`

**Input:** Prepared document collection and user search query.

**Output:** Ranked documents with IDs, titles, and similarity scores.

**Acceptance Criteria:**

- TF-IDF vectorizer fitted on documents only.
- Query transformation using the existing fitted vectorizer.
- Correct cosine similarity computation.
- Descending score ordering.
- Configurable Top-K retrieval.
- At least three ranked search demonstrations.
- Explanation of the highest-ranked result.
- Functional integrated Python console application.

## 4. Module Dependencies

| Module | Depends On |
|---|---|
| Dataset Engineering | Original TREC-COVID corpus |
| Text Preprocessing | Dataset Engineering |
| Inverted Index | Dataset and Text Preprocessing |
| Boolean Search | Inverted Index and Text Preprocessing |
| Ranked Search | Dataset and Text Preprocessing |
| System Integration | All implemented modules |

## 5. Shared Responsibilities

All team members must:

- Work on their assigned GitHub branches.
- Maintain individual Git commits.
- Test their implemented modules.
- Document actual development progress.
- Provide reproducible test results.
- Open pull requests for completed work.
- Participate in system integration.
- Participate in the recorded project presentation.
- Cite external code, datasets, and AI assistance.

## 6. Task Approval Process

A task will be considered completed after:

1. Implementation of the assigned functionality.
2. Successful module testing.
3. Documentation of actual results.
4. Pull request submission.
5. Code review by the team leader.
6. Successful integration into the main branch.

## 7. Development Status

This document represents the planned task allocation and module acceptance criteria.

Actual implementation progress, individual contributions, test results, and integration activities will be recorded throughout project development.
