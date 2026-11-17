# Project Progress Log

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| University | Al al-Bayt University |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Size | 5 Members |
| Project Leader | محمد بهجت فهمي علي |
| Submission Deadline | November 18, 2026 |
| Last Updated | November 17, 2026 |
| Current Status | Technical Implementation Completed |

---

## 2. Purpose

This progress log documents the development activities, technical milestones, implementation results, integration activities, and testing outcomes of the Medical Research Search project.

The log distinguishes completed technical activities from pending documentation and submission activities.

---

## 3. Development Timeline

| Date | Development Stage | Status |
|---|---|---|
| November 16, 2026 | Project Planning and Repository Organization | Completed |
| November 16, 2026 | Proposal Documentation | Completed |
| November 16, 2026 | Team Responsibilities and Development Workflow | Established |
| November 17, 2026 | Dataset Acquisition and Preparation | Completed |
| November 17, 2026 | NLP Preprocessing | Completed |
| November 17, 2026 | Inverted Index Construction | Completed |
| November 17, 2026 | Boolean Search Implementation | Completed |
| November 17, 2026 | TF-IDF and Ranked Retrieval | Completed |
| November 17, 2026 | System Integration | Completed |
| November 17, 2026 | Automated System Testing | Completed |
| November 17, 2026 | Main Repository Documentation | Completed |
| November 17, 2026 | Final Teamwork Documentation | In Progress |
| November 18, 2026 | Submission Deadline | Scheduled |

The dates represent documented development milestones and repository activities rather than individual working hours.

---

## 4. Progress Entry 01 — Project Planning

**Date:** November 16, 2026

**Related Stage:** Step 01 and Step 02

### Activities

- Define the medical research information retrieval problem.
- Establish the project objectives.
- Identify the required retrieval features.
- Organize the repository structure.
- Define individual technical responsibilities.
- Establish the modular development workflow.
- Prepare dedicated development branches.
- Define project milestones and expected deliverables.

### Outcome

The project requirements, technical responsibilities, and development structure were established.

### Evidence

- [Project Proposal](../Step_01_Proposal/)
- [Task Allocation](task_allocation.md)
- [Development Workflow](development_workflow.md)
- [Project Milestones](milestones.md)

**Status:** Completed

---

## 5. Progress Entry 02 — Dataset Engineering

**Date:** November 17, 2026

**Related Stage:** Step 03

**Assigned Responsibility:** Mashhour Rami — Dataset Engineering

### Activities

- Acquire the BEIR TREC-COVID research corpus.
- Validate required document fields.
- Remove records with missing information.
- Detect duplicate content.
- Remove non-searchable records.
- Select a reproducible subset using a fixed random seed.
- Generate the structured CSV collection.
- Record dataset preparation statistics.

### Actual Results

| Metric | Result |
|---|---:|
| Examined Records | 171,332 |
| Rejected Records | 42,383 |
| Valid Candidate Records | 128,949 |
| Selected Documents | 1,000 |
| Random Seed | 42 |

### Evidence

- [Dataset Acquisition Script](../Step_03_Preprocessing/download_dataset.py)
- [Dataset Report](../Step_03_Preprocessing/dataset/dataset_report.json)

**Status:** Completed

---

## 6. Progress Entry 03 — NLP Preprocessing

**Date:** November 17, 2026

**Related Stage:** Step 03

**Assigned Responsibility:** Omar Atiyeh — NLP Preprocessing

### Activities

- Implement text normalization.
- Apply lowercasing.
- Implement regular expression tokenization.
- Apply configurable stopword removal.
- Apply Porter Stemming.
- Establish shared preprocessing functions.
- Generate preprocessing demonstration results.

### Demonstrated Output

Original text:

```text
COVID-19 vaccines are reducing infections.
```

Final processed terms:

```text
['covid', '19', 'vaccin', 'reduc', 'infect']
```

### Outcome

A shared text preprocessing pipeline was established for document indexing, Boolean retrieval, and ranked retrieval.

### Evidence

- [Preprocessing Implementation](../Step_03_Preprocessing/preprocessing.py)
- [Preprocessing Results](../Step_03_Preprocessing/preprocessing_results.txt)

**Status:** Completed

---

## 7. Progress Entry 04 — Inverted Index

**Date:** November 17, 2026

**Related Stage:** Step 04

**Assigned Responsibility:** Laith Jaber — Inverted Index

### Activities

- Construct a dictionary-based inverted index.
- Associate processed terms with document posting sets.
- Calculate document frequency statistics.
- Validate index construction.
- Connect the index with Boolean retrieval.

### Actual Results

| Metric | Result |
|---|---:|
| Indexed Documents | 1,000 |
| Unique Vocabulary Terms | 10,758 |
| Total Postings | 87,381 |
| Documents Without Searchable Terms | 0 |

### Evidence

- [Inverted Index Implementation](../Step_04_Boolean_Search/inverted_index.py)
- [Index Results](../Step_04_Boolean_Search/index_results.txt)

**Status:** Completed

---

## 8. Progress Entry 05 — Boolean Retrieval

**Date:** November 17, 2026

**Related Stage:** Step 04

**Assigned Responsibility:** Mohammad Saleh — Boolean Retrieval

### Activities

- Implement AND, OR, and NOT operations.
- Support compound Boolean expressions.
- Implement operator precedence.
- Support parentheses.
- Validate invalid query handling.
- Demonstrate Boolean search on the prepared collection.

### Actual Results

| Query | Matching Documents |
|---|---:|
| covid AND vaccine | 21 |
| covid OR vaccine | 357 |
| NOT vaccine | 923 |
| covid AND NOT vaccine | 280 |
| (covid OR virus) AND vaccine | 53 |

### Outcome

Boolean retrieval successfully evaluated logical expressions against the complete indexed document collection.

### Evidence

- [Boolean Search Implementation](../Step_04_Boolean_Search/boolean_search.py)
- [Boolean Search Results](../Step_04_Boolean_Search/boolean_results.txt)

**Status:** Completed

---

## 9. Progress Entry 06 — TF-IDF and Ranked Retrieval

**Date:** November 17, 2026

**Related Stage:** Step 05

**Assigned Responsibility:** Team Leader — Ranked Retrieval

### Activities

- Implement TF-IDF document vectorization.
- Construct a sparse document-term matrix.
- Implement query vectorization.
- Calculate cosine similarity.
- Implement descending document ranking.
- Support configurable Top-K retrieval.
- Add term-level ranking explanations.
- Execute ranked retrieval demonstrations.
- Execute automated component self-tests.

### Actual System Statistics

| Metric | Result |
|---|---:|
| Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Nonzero TF-IDF Weights | 87,381 |
| Demonstrated Queries | 3 |
| Results per Demonstration Query | 5 |

### Ranked Retrieval Results

| Query | Highest Similarity Score |
|---|---:|
| covid vaccine immune response | 0.451483 |
| respiratory infection treatment | 0.331911 |
| coronavirus transmission prevention | 0.279990 |

Component self-tests passed successfully.

### Evidence

- [Ranked Search Implementation](../Step_05_Ranked_Search/ranked_search.py)
- [Ranked Search Results](../Step_05_Ranked_Search/ranking_results.txt)

**Status:** Completed

---

## 10. Progress Entry 07 — System Integration

**Date:** November 17, 2026

**Assigned Responsibility:** Team Leader — System Integration

### Activities

- Integrate the existing retrieval modules.
- Configure automatic module imports.
- Establish project-relative dataset loading.
- Connect the shared NLP preprocessing pipeline.
- Integrate inverted index construction.
- Integrate Boolean retrieval.
- Integrate TF-IDF ranked retrieval.
- Implement the unified command-line interface.
- Support Unicode output.
- Execute the complete system demonstration.
- Compare integrated results with standalone component results.

### Integration Results

| Validation Area | Result |
|---|---|
| Dataset Loading | PASS |
| NLP Preprocessing | PASS |
| Inverted Index Construction | PASS |
| Boolean Retrieval | PASS |
| TF-IDF Matrix Construction | PASS |
| Ranked Retrieval | PASS |
| Ranking Explanations | PASS |
| Full Integrated Demonstration | PASS |

All five Boolean demonstration match counts and all three ranked search demonstrations remained consistent after integration.

### Evidence

- [Unified Application](../Integration/main.py)
- [Integration Results](../Integration/integration_results.txt)
- [Integration Documentation](../Integration/README.md)

**Status:** Completed

---

## 11. Progress Entry 08 — Automated System Testing

**Date:** November 17, 2026

**Assigned Responsibility:** System Testing and Quality Assurance

### Activities

- Implement automated tests using Python unittest.
- Test controlled synthetic document collections.
- Test the real 1,000-document collection.
- Validate dataset integrity.
- Validate preprocessing and inverted indexing.
- Validate Boolean retrieval operations.
- Validate ranked retrieval behavior.
- Validate invalid inputs and edge cases.
- Test interactive application behavior.
- Verify portable execution.
- Perform regression testing.

### Actual Results

| Metric | First Execution | Second Execution |
|---|---:|---:|
| Total Tests | 15 | 15 |
| Passed | 15 | 15 |
| Failed | 0 | 0 |
| Errors | 0 | 0 |
| Test Pass Rate | 100% | 100% |
| Execution Time | 10.161s | 8.257s |

The test suite included nine synthetic tests and six real corpus tests.

### Final Recorded Output

```text
----------------------------------------------------------------------
Ran 15 tests in 8.257s

OK
```

### Evidence

- [Automated Test Implementation](../Testing/test_system.py)
- [Actual Test Results](../Testing/test_results.txt)
- [Testing Documentation](../Testing/README.md)

**Status:** Completed

---

## 12. Progress Entry 09 — Technical Documentation

**Date:** November 17, 2026

### Activities

- Complete the individual component README files.
- Document the implemented retrieval algorithms.
- Document actual execution statistics.
- Document system architecture and dependencies.
- Add integrated execution evidence.
- Add automated testing evidence.
- Complete the main repository README.
- Document installation and execution instructions.
- Document technical limitations and future improvements.
- Acknowledge external references and AI assistance.

### Repository Checkpoint

The repository displayed 60 commits at the checkpoint immediately following the main README update on November 17, 2026.

This value represents a historical checkpoint rather than the final repository commit count.

### Evidence

- [Main README](../README.md)
- [Repository History](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/commits/main/)

**Status:** Completed

---

## 13. Progress Entry 10 — Final Teamwork Documentation

**Date:** November 17, 2026

### Activities

- Update team responsibilities.
- Link technical deliverables to the corresponding assigned modules.
- Update contribution documentation.
- Record completed milestones.
- Document integration and repository activities.
- Organize authentic collaboration evidence.
- Distinguish assigned responsibilities from verified individual authorship.

### Evidence

- [Team Contributions](contributions.md)
- [Task Allocation](task_allocation.md)
- [Milestones](milestones.md)
- [Integration Log](integration_log.md)

**Status:** In Progress

---

## 14. Technical Challenges and Resolutions

| Challenge | Implemented Resolution | Status |
|---|---|---|
| Missing and invalid dataset fields | Dataset validation and filtering | Resolved |
| Duplicate document content | Duplicate detection | Resolved |
| Vocabulary variations | Shared NLP preprocessing | Resolved |
| Complex Boolean expressions | Logical precedence and expression evaluation | Resolved |
| High-dimensional document vectors | Sparse TF-IDF representation | Addressed |
| Unexplained ranking scores | Shared term contribution explanations | Addressed |
| Distributed module directories | Automatic module path configuration | Resolved |
| Windows Unicode output errors | UTF-8 output configuration | Resolved |
| Potential integration regressions | Automated regression testing | Validated |

---

## 15. Project Milestone Summary

| Milestone | Status |
|---|---|
| Problem Definition | Completed |
| Project Proposal | Completed |
| Task Allocation | Established |
| Dataset Engineering | Completed |
| NLP Preprocessing | Completed |
| Inverted Index | Completed |
| Boolean Retrieval | Completed |
| TF-IDF Ranked Retrieval | Completed |
| System Integration | Completed |
| Automated System Testing | Completed |
| Main Repository README | Completed |
| Final Teamwork Documentation | In Progress |
| Final Submission Materials | Pending |
| Presentation Video | Pending |

---

## 16. Final Technical Progress Summary

| Metric | Recorded Result |
|---|---:|
| Prepared Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Inverted Index Postings | 87,381 |
| Nonzero TF-IDF Weights | 87,381 |
| Boolean Demonstration Queries | 5 |
| Ranked Demonstration Queries | 3 |
| Automated System Tests | 15 |
| Passed System Tests | 15 |
| Failed System Tests | 0 |
| Functional Test Pass Rate | 100% |

The project has successfully demonstrated its complete technical retrieval pipeline.

The recorded test pass rate applies to the executed functional tests and does not represent retrieval relevance accuracy.

---

## 17. Remaining Activities

- Finalize teamwork documentation.
- Verify individual contribution evidence.
- Finalize the submission directory.
- Prepare the project demonstration video.
- Confirm submission requirements.
- Update final repository completion status.
- Submit the required project materials before the deadline.

---

## 18. Progress Verification

This progress log is based on documented project milestones, repository checkpoints, implementation files, and actual execution outputs.

Assigned responsibilities do not independently establish individual commit authorship.

Unverified working hours, meeting attendance, contribution percentages, and unsupported activities are not included.

AI assistance was used to support implementation, debugging, testing, and documentation.

---

**Medical Research Search**

Al al-Bayt University

Information Retrieval Systems — Phase 1

Last Updated: November 17, 2026
