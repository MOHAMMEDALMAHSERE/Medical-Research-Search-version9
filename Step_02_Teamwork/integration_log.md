# System Integration and Code Review Log

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| Course | Information Retrieval Systems (902333) |
| University | Al al-Bayt University |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Students |
| Approximate Project Start | November 12, 2026 |
| Target Integration Date | November 17, 2026 |
| Final Submission | November 18, 2026 |

## 2. Purpose

This document records the integration of individual technical modules into a unified Information Retrieval System.

The integration process ensures that all independently developed components operate together using consistent data structures, compatible interfaces, and verified functionality.

The team leader is responsible for coordinating code reviews, approving technical contributions, resolving integration issues, and maintaining the integrated system.

## 3. Module Integration Overview

| Module | Responsible Member | Branch | Integration Status |
|---|---|---|---|
| Dataset Acquisition and Cleaning | Mashhour Rami | mashhour-rami | Pending |
| NLP and Text Preprocessing | Omar Atiyeh | omar-atiyeh | Pending |
| Inverted Index | Laith Jaber | laith-jaber | Pending |
| Boolean Search | Mohammad Saleh | mohammad-saleh | Pending |
| TF-IDF and Ranked Search | Team Leader | Leader development branch | Pending |
| Main Application | Team Leader | Integration / main | Pending |
| System Validation | All Members | main | Pending |

## 4. Planned Integration Sequence

### Integration Stage 01 — Dataset Preparation

**Module Owner:** Mashhour Rami

**Integration Coordinator:** Team Leader

**Required Components:**

- Dataset acquisition script.
- Data cleaning functionality.
- Structured document collection.
- Dataset validation report.

**Integration Requirements:**

- Unique document identifiers.
- Valid document titles and text.
- At least 100 distinct documents, targeting 1,000.
- Reproducible dataset acquisition and sampling.
- Consistent CSV structure.

**Expected Output:** Clean document collection ready for preprocessing.

**Status:** Pending.

### Integration Stage 02 — Text Preprocessing

**Module Owner:** Omar Atiyeh

**Integration Coordinator:** Team Leader

**Required Components:**

- Text normalization.
- Lowercasing.
- Tokenization.
- Configurable stopword handling.
- Stemming or lemmatization.

**Integration Requirements:**

- Consistent processing of documents and queries.
- Reusable preprocessing functions.
- Compatibility with Boolean and ranked retrieval.
- Safe handling of empty text.

**Expected Output:** Processed searchable document terms.

**Status:** Pending.

### Integration Stage 03 — Inverted Index

**Module Owner:** Laith Jaber

**Integration Coordinator:** Team Leader

**Required Components:**

- Term-to-document mappings.
- Posting lists.
- Complete indexed document ID set.
- Document metadata lookup.

**Integration Requirements:**

- Compatibility with the shared preprocessing pipeline.
- Correct Python dictionary and set structures.
- Valid document identifiers.
- Correct handling of unknown terms.

**Expected Output:** Functional inverted index.

**Status:** Pending.

### Integration Stage 04 — Boolean Retrieval

**Module Owner:** Mohammad Saleh

**Integration Coordinator:** Team Leader

**Required Components:**

- Boolean query parsing.
- AND operation.
- OR operation.
- NOT operation.
- Document retrieval functionality.

**Integration Requirements:**

- Compatibility with the inverted index.
- Preservation of Boolean operators during preprocessing.
- Correct set operations.
- NOT evaluated against the complete indexed document set.
- Display of matching document IDs and titles.
- Handling of empty and invalid queries.

**Expected Output:** Functional Boolean search engine.

**Status:** Pending.

### Integration Stage 05 — Ranked Retrieval

**Module Owner:** Team Leader

**Required Components:**

- TF-IDF document vectorization.
- Fitted vectorizer.
- Query transformation.
- Cosine similarity computation.
- Descending document ranking.
- Top-K retrieval.

**Integration Requirements:**

- Use the same prepared document collection as Boolean retrieval.
- Apply consistent text preprocessing.
- Fit the vectorizer on the document collection only.
- Transform queries without refitting.
- Return actual document IDs, titles, ranks, and similarity scores.
- Handle empty and unknown-term queries.

**Expected Output:** Functional ranked search engine.

**Status:** Pending.

### Integration Stage 06 — Main Application

**Module Owner:** Team Leader

**Required Components:**

- Shared document collection.
- Text preprocessing module.
- Inverted index.
- Boolean retrieval engine.
- Ranked retrieval engine.
- Python console interface.

**Integration Requirements:**

- All components operate within one application.
- Both retrieval methods use the same document collection.
- Search results are generated dynamically.
- Dependencies are documented.
- Application execution commands are available.
- Critical integration errors are resolved.

**Expected Output:** Complete integrated Information Retrieval System.

**Status:** Pending.

## 5. Shared Data Schema

All integrated modules will use the following document structure:

| Field | Data Type | Description |
|---|---|---|
| document_id | String | Unique document identifier |
| title | String | Original research document title |
| text | String | Original searchable document content |
| source | String | Dataset provenance |

The searchable document content will combine the title and text.

Document identifiers must remain consistent throughout dataset preparation, indexing, Boolean retrieval, and ranked retrieval.

## 6. Code Review Checklist

Each technical contribution will be reviewed before final integration.

- [ ] Assigned functionality implemented.
- [ ] Module acceptance criteria satisfied.
- [ ] Source code readable and organized.
- [ ] Input and output structures compatible.
- [ ] Required dependencies documented.
- [ ] Individual module tests executed.
- [ ] Actual testing results documented.
- [ ] Empty and invalid inputs handled appropriately.
- [ ] No hard-coded search results.
- [ ] External sources and AI assistance acknowledged.
- [ ] Pull request reviewed.
- [ ] Contribution approved for integration.

## 7. Pull Request and Merge Tracking

| Contributor | Module | Pull Request | Review Status | Merge Status |
|---|---|---|---|---|
| Mashhour Rami | Dataset Engineering | Pending | Pending | Not Merged |
| Omar Atiyeh | Text Preprocessing | Pending | Pending | Not Merged |
| Laith Jaber | Inverted Index | Pending | Pending | Not Merged |
| Mohammad Saleh | Boolean Search | Pending | Pending | Not Merged |
| Team Leader | Ranked Search | Pending | Pending | Not Merged |
| Team Leader | Main Application | Pending | Pending | Not Merged |

Actual pull request links, review outcomes, merge commit identifiers, and completion dates will be recorded after the corresponding activities.

## 8. Integration Activity Log

| Date | Module | Activity | Responsible Member | Result | Evidence |
|---|---|---|---|---|---|
| November 17, 2026 (Target) | Dataset | Dataset integration | Team Leader / Mashhour Rami | Pending | Pending |
| November 17, 2026 (Target) | Preprocessing | Pipeline integration | Team Leader / Omar Atiyeh | Pending | Pending |
| November 17, 2026 (Target) | Inverted Index | Index integration | Team Leader / Laith Jaber | Pending | Pending |
| November 17, 2026 (Target) | Boolean Search | Retrieval integration | Team Leader / Mohammad Saleh | Pending | Pending |
| November 17, 2026 (Target) | Ranked Search | Ranking integration | Team Leader | Pending | Pending |
| November 17, 2026 (Target) | Main Application | Complete system integration | Team Leader | Pending | Pending |

The dates listed above are planned integration targets and do not represent completed activities.

## 9. Integration Issue Tracking

| Issue ID | Related Module | Description | Resolution | Status |
|---|---|---|---|---|
| — | — | No integration issues recorded yet | — | — |

Actual integration issues will be documented during implementation and testing.

## 10. Final System Validation

| Validation Requirement | Expected Result | Actual Status |
|---|---|---|
| Dataset Loading | Valid document collection loaded successfully | Pending |
| Dataset Quality | Unique and meaningful searchable documents | Pending |
| Text Preprocessing | Consistent processed terms | Pending |
| Inverted Index | Correct posting lists | Pending |
| Boolean AND | Correct intersection results | Pending |
| Boolean OR | Correct union results | Pending |
| Boolean NOT | Correct complement results | Pending |
| TF-IDF | Valid document and query vectors | Pending |
| Cosine Similarity | Correct similarity computation | Pending |
| Ranked Retrieval | Descending Top-K results | Pending |
| Ranked Demonstrations | At least three search examples | Pending |
| Empty Query Handling | Safe and controlled response | Pending |
| Main Application | Successful console execution | Pending |
| Reproducibility | Consistent results using the same configuration | Pending |

## 11. Integration Record Template

Each completed integration activity should include:

- Integration date:
- Module name:
- Module owner:
- Reviewed files:
- Commit link:
- Pull request link:
- Code review outcome:
- Tests performed:
- Actual test results:
- Identified issues:
- Applied corrections:
- Merge commit:
- Integration result:
- Approval status:

## 12. Integration Completion Criteria

The integrated system will be considered completed when:

- All required technical modules have been implemented.
- Individual module tests have been performed.
- All required components have been successfully integrated.
- Both retrieval approaches use the same document collection.
- Boolean queries return correct matching documents.
- Ranked queries return valid cosine similarity scores.
- At least three ranked retrieval demonstrations are documented.
- Empty queries are handled appropriately.
- The main application executes successfully.
- Actual integration and testing evidence is available.
- Installation and execution instructions are documented.

## 13. Academic Evidence Policy

Integration records must accurately represent actual development activities.

Completed integration activities must be supported by relevant evidence, including Git commits, pull requests, code review records, execution logs, and testing results.

Individual technical contributions must remain correctly attributed to their actual contributors.

Planned integration activities must not be reported as successfully completed before verification.

## 14. Current Status

The integration strategy, module dependencies, review procedures, and validation requirements have been established.

Technical implementation and system integration are pending.

The target date for complete system integration and validation is November 17, 2026.

This document will be updated following actual code reviews, module integration, and system testing.

---

**Medical Research Search**

Information Retrieval Systems (902333)

Al al-Bayt University — Phase 1
