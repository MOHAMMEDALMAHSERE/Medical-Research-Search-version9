# Project Evidence and Verification Register

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| University | Al al-Bayt University |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Members |
| Repository | Medical-Research-Search-version9 |
| Last Updated | November 17, 2026 |
| Technical Validation | 15/15 Tests Passed |

---

## 2. Purpose

This evidence register provides centralized access to the implementation files, actual execution results, technical documentation, development history, and available collaboration evidence of the Medical Research Search project.

The primary objectives are to:

- Support transparent project evaluation.
- Provide traceable technical deliverables.
- Document actual system execution.
- Verify completed technical milestones.
- Provide access to development branches and pull requests.
- Support individual contribution verification.
- Maintain academic integrity.
- Avoid unnecessary duplication of evidence files.

All technical evidence is linked directly to its original location within the repository.

---

## 3. Evidence Classification

| Evidence Category | Description |
|---|---|
| Implementation Evidence | Python source code and technical modules |
| Dataset Evidence | Dataset preparation reports and collection statistics |
| Execution Evidence | Actual preprocessing and retrieval outputs |
| Integration Evidence | Unified application execution results |
| Testing Evidence | Automated functional and regression test results |
| Repository Evidence | Git branches, commits and pull requests |
| Teamwork Evidence | Assigned responsibilities and progress documentation |
| Presentation Evidence | Final demonstration and individual explanations |

---

## 4. Master Evidence Register

| Evidence ID | Technical Area | Evidence File | Status |
|---|---|---|---|
| EV-01 | Project Proposal | [phase1-proposal.docx](../../Step_01_Proposal/phase1-proposal.docx) | Available |
| EV-02 | Task Allocation | [task_allocation.md](../task_allocation.md) | Available |
| EV-03 | Dataset Acquisition | [download_dataset.py](../../Step_03_Preprocessing/download_dataset.py) | Available |
| EV-04 | Dataset Preparation | [dataset_report.json](../../Step_03_Preprocessing/dataset/dataset_report.json) | Available |
| EV-05 | NLP Implementation | [preprocessing.py](../../Step_03_Preprocessing/preprocessing.py) | Available |
| EV-06 | NLP Execution | [preprocessing_results.txt](../../Step_03_Preprocessing/preprocessing_results.txt) | Available |
| EV-07 | Inverted Index | [inverted_index.py](../../Step_04_Boolean_Search/inverted_index.py) | Available |
| EV-08 | Index Statistics | [index_results.txt](../../Step_04_Boolean_Search/index_results.txt) | Available |
| EV-09 | Boolean Retrieval | [boolean_search.py](../../Step_04_Boolean_Search/boolean_search.py) | Available |
| EV-10 | Boolean Execution | [boolean_results.txt](../../Step_04_Boolean_Search/boolean_results.txt) | Available |
| EV-11 | Ranked Retrieval | [ranked_search.py](../../Step_05_Ranked_Search/ranked_search.py) | Available |
| EV-12 | Ranked Execution | [ranking_results.txt](../../Step_05_Ranked_Search/ranking_results.txt) | Available |
| EV-13 | System Integration | [main.py](../../Integration/main.py) | Available |
| EV-14 | Integration Execution | [integration_results.txt](../../Integration/integration_results.txt) | Available |
| EV-15 | Automated Testing | [test_system.py](../../Testing/test_system.py) | Available |
| EV-16 | Test Execution | [test_results.txt](../../Testing/test_results.txt) | Available |
| EV-17 | Main Documentation | [README.md](../../README.md) | Available |
| EV-18 | Presentation Video | Final Submission | Pending |

---

## 5. GitHub Repository Evidence

### Repository Information

| Property | Description |
|---|---|
| Repository Platform | GitHub |
| Version Control | Git |
| Main Branch | main |
| Development Strategy | Component-Based Branching |
| Integration Method | Pull Requests and Centralized Integration |

### Repository Links

- [Main Repository](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9)
- [Commit History](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/commits/main/)
- [Development Branches](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/branches)
- [Pull Requests](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pulls?q=is%3Apr)
- [Repository Contributors](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/graphs/contributors)

### Recorded Repository Checkpoint

At the development checkpoint following the main README update on November 17, 2026:

- The repository displayed 60 commits.
- The technical project directories were organized.
- The integrated application was available.
- Automated testing evidence was available.
- The main project documentation had been completed.

The recorded commit count represents a historical checkpoint and may increase as final documentation is completed.

---

## 6. Pull Request Evidence

| Evidence ID | Pull Request | Assigned Technical Component |
|---|---|---|
| PR-EV-01 | [Pull Request #1](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/1) | Dataset Engineering |
| PR-EV-02 | [Pull Request #2](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/2) | NLP Preprocessing |
| PR-EV-03 | [Pull Request #3](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/3) | Inverted Index |
| PR-EV-04 | [Pull Request #4](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/4) | Boolean Retrieval |
| PR-EV-05 | [Pull Request #5](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/5) | Ranked Retrieval |

The corresponding GitHub records provide access to actual changes, authorship, timestamps, and integration history.

Pull request existence alone does not establish independent contribution by the assigned team member.

---

## 7. Dataset Engineering Evidence

**Assigned Responsibility:** Mashhour Rami

### Recorded Results

| Metric | Actual Result |
|---|---:|
| Examined Records | 171,332 |
| Missing-Field Records | 42,146 |
| Non-searchable Records | 51 |
| Duplicate Identifiers | 0 |
| Duplicate Content Records | 186 |
| Total Rejected Records | 42,383 |
| Valid Candidate Records | 128,949 |
| Selected Documents | 1,000 |
| Random Seed | 42 |

### Supporting Evidence

- [Dataset Acquisition Script](../../Step_03_Preprocessing/download_dataset.py)
- [Dataset Preparation Report](../../Step_03_Preprocessing/dataset/dataset_report.json)
- [Dataset Documentation](../../Step_03_Preprocessing/README.md)

The prepared collection is based on the BEIR TREC-COVID corpus.

Dataset contents remain subject to applicable source licensing and redistribution conditions.

---

## 8. NLP Preprocessing Evidence

**Assigned Responsibility:** Omar Atiyeh

### Demonstrated Input

```text
COVID-19 vaccines are reducing infections.
```

### Tokenization

```text
['covid', '19', 'vaccines', 'are', 'reducing', 'infections']
```

### Stopword Removal

```text
['covid', '19', 'vaccines', 'reducing', 'infections']
```

### Final Stemmed Terms

```text
['covid', '19', 'vaccin', 'reduc', 'infect']
```

### Verified Technical Areas

- Text normalization.
- Lowercasing.
- Tokenization.
- Stopword removal.
- Porter Stemming.
- Shared preprocessing across retrieval modules.

### Supporting Evidence

- [Preprocessing Implementation](../../Step_03_Preprocessing/preprocessing.py)
- [Actual Preprocessing Results](../../Step_03_Preprocessing/preprocessing_results.txt)
- [Integrated Preprocessing Demonstration](../../Integration/integration_results.txt)

---

## 9. Inverted Index Evidence

**Assigned Responsibility:** Laith Jaber

### Recorded Results

| Metric | Actual Result |
|---|---:|
| Indexed Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Total Postings | 87,381 |
| Documents Without Searchable Terms | 0 |
| Document Frequency of covid | 301 |
| Document Frequency of vaccine | 77 |
| Document Frequency of virus | 253 |

Document frequencies refer to the corresponding processed search terms.

### Supporting Evidence

- [Inverted Index Implementation](../../Step_04_Boolean_Search/inverted_index.py)
- [Actual Index Statistics](../../Step_04_Boolean_Search/index_results.txt)

---

## 10. Boolean Retrieval Evidence

**Assigned Responsibility:** Mohammad Saleh

### Recorded Search Results

| Query | Matching Documents |
|---|---:|
| covid AND vaccine | 21 |
| covid OR vaccine | 357 |
| NOT vaccine | 923 |
| covid AND NOT vaccine | 280 |
| (covid OR virus) AND vaccine | 53 |

All five demonstration match counts were reproduced successfully after system integration.

### Supporting Evidence

- [Boolean Retrieval Implementation](../../Step_04_Boolean_Search/boolean_search.py)
- [Actual Boolean Search Results](../../Step_04_Boolean_Search/boolean_results.txt)
- [Integration Regression Results](../../Integration/integration_results.txt)

---

## 11. Ranked Retrieval Evidence

**Assigned Responsibility:** Mohammed Ali — Team Leader

### TF-IDF Statistics

| Metric | Actual Result |
|---|---:|
| Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Matrix Shape | 1,000 × 10,758 |
| Nonzero TF-IDF Weights | 87,381 |
| Demonstrated Queries | 3 |
| Results per Query | 5 |

### Actual Ranking Results

| Query | Highest-Ranked Document ID | Cosine Similarity |
|---|---|---:|
| covid vaccine immune response | 6fhuon6k | 0.451483 |
| respiratory infection treatment | yqr3e4kp | 0.331911 |
| coronavirus transmission prevention | nlzdto1h | 0.279990 |

### Ranking Explanation Example

| Shared Term | Contribution |
|---|---:|
| immun | 0.222565 |
| respons | 0.144711 |
| vaccin | 0.084207 |
| Total | 0.451483 |

The similarity score represents lexical relevance rather than clinical reliability.

### Supporting Evidence

- [Ranked Retrieval Implementation](../../Step_05_Ranked_Search/ranked_search.py)
- [Actual Ranking Results](../../Step_05_Ranked_Search/ranking_results.txt)

---

## 12. System Integration Evidence

**Assigned Responsibility:** Mohammed Ali — Team Leader

### Integrated Components

- Dataset loading.
- Shared NLP preprocessing.
- Inverted index construction.
- Boolean retrieval.
- TF-IDF document representation.
- Cosine similarity.
- Ranked retrieval.
- Ranking explanations.
- Unified command-line interface.

### Validation Summary

| Validation Area | Result |
|---|---|
| Dataset Loading | PASS |
| NLP Preprocessing | PASS |
| Inverted Index Construction | PASS |
| Boolean Retrieval | PASS |
| TF-IDF Construction | PASS |
| Ranked Retrieval | PASS |
| Ranking Explanations | PASS |
| Full Integrated Demonstration | PASS |

### Recorded Execution Output

```text
Demo completed successfully.
```

### Supporting Evidence

- [Unified Application](../../Integration/main.py)
- [Actual Integration Results](../../Integration/integration_results.txt)
- [Integration Documentation](../../Integration/README.md)

---

## 13. Automated Testing Evidence

The integrated system was tested using Python unittest.

### Test Distribution

| Test Category | Total | Passed | Failed |
|---|---:|---:|---:|
| Synthetic Tests | 9 | 9 | 0 |
| Real Corpus Tests | 6 | 6 | 0 |
| Total | 15 | 15 | 0 |

### Recorded Execution History

| Execution | Tests Passed | Failures | Duration |
|---|---:|---:|---:|
| First Execution | 15 | 0 | 10.161s |
| Second Execution | 15 | 0 | 8.257s |

### Final Recorded Output

```text
----------------------------------------------------------------------
Ran 15 tests in 8.257s

OK
```

### Verified Test Areas

- Dataset integrity.
- NLP preprocessing.
- Inverted index construction.
- Boolean logic.
- Invalid Boolean expressions.
- Invalid CSV files.
- Ranked retrieval.
- Empty and unknown queries.
- Top-K retrieval.
- Similarity score bounds.
- Ranking ties.
- Interactive application behavior.
- Portable execution.
- Boolean regression.
- Ranked regression.

### Supporting Evidence

- [Automated Test Implementation](../../Testing/test_system.py)
- [Actual Test Execution Results](../../Testing/test_results.txt)
- [Testing Documentation](../../Testing/README.md)

The recorded 100% test pass rate applies to the implemented functional test suite. It does not establish perfect retrieval relevance or complete code coverage.

---

## 14. Team Responsibility and Evidence Mapping

| Assigned Team Member | Technical Area | Main Supporting Evidence |
|---|---|---|
| محمد بهجت فهمي علي | Ranked Retrieval, Integration and Testing | EV-11 to EV-17 |
| مشهور رامي مشهور أبو سنينة | Dataset Engineering | EV-03 and EV-04 |
| عمر عبد الباسط محمود عطية | NLP Preprocessing | EV-05 and EV-06 |
| ليث بسام محمود جابر | Inverted Index | EV-07 and EV-08 |
| محمد مثنى محمد خالد صالح | Boolean Retrieval | EV-09 and EV-10 |

This mapping identifies the technical evidence associated with each assigned responsibility.

It does not independently verify who authored every source code change.

---

## 15. Individual Contribution Verification

Individual participation should be established through authentic records.

| Evidence Type | Verification Purpose |
|---|---|
| GitHub Commits | Identify actual recorded code authorship |
| Pull Requests | Track component changes and integration |
| Original Submitted Files | Support individual implementation attribution |
| Communication Records | Support actual team coordination |
| Technical Demonstrations | Demonstrate understanding of assigned components |
| Presentation Video | Document individual explanations and participation |

The repository displayed one GitHub contributor at the observed November 17, 2026 checkpoint.

Therefore, additional authentic evidence may be necessary to demonstrate individual participation beyond repository-level statistics.

No fabricated screenshots, commit histories, contribution percentages, or meeting attendance records are included.

---

## 16. Phase 1 Assessment Traceability

| Step | Assessment Area | Marks Allocated | Supporting Evidence |
|---|---|---:|---|
| 01 | Problem Definition and Proposal | 3 | EV-01 |
| 02 | Progress and Teamwork | 3 | EV-02, Teamwork Documentation, GitHub Records |
| 03 | Dataset and NLP Preprocessing | 3 | EV-03 to EV-06 |
| 04 | Inverted Index and Boolean Retrieval | 3 | EV-07 to EV-10 |
| 05 | TF-IDF and Ranked Retrieval | 4 | EV-11 and EV-12 |
| Additional Validation | Integration and Testing | Supporting Evidence | EV-13 to EV-17 |

Total allocated Phase 1 marks: 16.

Allocated marks represent the assessment structure, not grades already awarded.

---

## 17. Evidence Verification Matrix

| Validation Area | Evidence Status |
|---|---|
| Project Proposal | Available |
| Assigned Responsibilities | Available |
| Dataset Preparation | Available |
| NLP Preprocessing | Available |
| Inverted Index | Available |
| Boolean Retrieval | Available |
| Ranked Retrieval | Available |
| System Integration | Available |
| Automated Testing | Available |
| Repository Development History | Available |
| Main Technical Documentation | Available |
| Individual Contribution Verification | Requires Authentic Supporting Records |
| Final Presentation Video | Pending |
| Final Submission | Pending |

---

## 18. Reproduction of Technical Evidence

All commands should be executed from the project root after installing the required dependencies and preparing the dataset.

### Execute the Unified Application

```bash
python -X utf8 Integration/main.py
```

### Execute the Full Demonstration

```powershell
python -X utf8 Integration/main.py --demo
```

### Regenerate Integration Evidence

```powershell
python -X utf8 Integration/main.py --demo | Tee-Object -FilePath Integration/integration_results.txt
```

### Execute Automated System Tests

```powershell
python -X utf8 Testing/test_system.py
```

### Regenerate Testing Evidence

```powershell
python -X utf8 Testing/test_system.py 2>&1 | Tee-Object -FilePath Testing/test_results.txt
```

Regression results require the original prepared document collection.

Execution times may vary depending on the development environment.

---

## 19. Final Technical Achievement Summary

| Metric | Recorded Result |
|---|---:|
| Prepared Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Inverted Index Postings | 87,381 |
| Nonzero TF-IDF Weights | 87,381 |
| Boolean Demonstration Queries | 5 |
| Ranked Demonstration Queries | 3 |
| Automated System Tests | 15 |
| Passed Tests | 15 |
| Failed Tests | 0 |
| Functional Test Pass Rate | 100% |
| Final Recorded Test Execution | 8.257 seconds |

---

## 20. Academic Integrity

All reported numerical results are based on recorded project execution outputs.

External datasets, libraries, and technical references are acknowledged in the project documentation.

AI assistance was used to support implementation, debugging, testing, technical review, and documentation.

Individual contribution claims must reflect actual work and should be supported by authentic evidence.

Private communication records should not be published without appropriate permission or removal of unnecessary personal information.

---

## 21. Related Documentation

- [Teamwork Overview](../README.md)
- [Team Contributions](../contributions.md)
- [Task Allocation](../task_allocation.md)
- [Progress Log](../progress_log.md)
- [Project Milestones](../milestones.md)
- [Development Workflow](../development_workflow.md)
- [Integration Log](../integration_log.md)
- [Meeting and Coordination Notes](../meeting_notes.md)
- [Main Project Documentation](../../README.md)
- [Final Submission](../../Final_Submission/)

---

**Medical Research Search**

Al al-Bayt University

Information Retrieval Systems — Phase 1

Last Updated: November 17, 2026
