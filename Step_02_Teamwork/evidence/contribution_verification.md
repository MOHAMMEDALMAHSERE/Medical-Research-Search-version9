# Team Contribution Verification Report

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| University | Al al-Bayt University |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Members |
| Verification Date | November 17, 2026 |
| Repository Commits at Verification | 69 |
| Verified Pull Requests | 5 |
| Successfully Merged Pull Requests | 5 |

## 2. Verification Methodology

The project repository was inspected to verify:

- Repository accessibility.
- Assigned technical components.
- Development branch names.
- Pull request existence.
- Pull request titles.
- Merge status.
- Merge dates.
- Commit identifiers.
- Integration into the main branch.
- Recorded repository account activity.
- Technical execution and testing evidence.

## 3. Verified Development Branches

| Assigned Member | Development Branch | Technical Component |
|---|---|---|
| مشهور رامي مشهور أبو سنينة | Mashhour-Rami | Dataset Engineering |
| عمر عبد الباسط محمود عطية | omar-atiyeh | NLP Preprocessing |
| ليث بسام محمود جابر | Laith-Jaber | Inverted Index |
| محمد مثنى محمد خالد صالح | Mohammad-Saleh | Boolean Retrieval |
| محمد بهجت فهمي علي | Mohammed-Ali | Ranked Retrieval |

All five branch names were verified through their associated pull request records.

## 4. Verified Pull Request Register

| PR | Component | Commits | Merge Commit | Status |
|---|---|---:|---|---|
| #1 | Dataset Acquisition and Cleaning | 3 | 0bf6f40 | Merged |
| #2 | NLP Text Preprocessing | 1 | b007807 | Merged |
| #3 | Inverted Index and Posting Lists | 1 | 1e0ccdd | Merged |
| #4 | Boolean Search and Query Processing | 1 | 693b7ca | Merged |
| #5 | TF-IDF and Ranked Retrieval | 1 | 587320b | Merged |

All five pull requests were merged into the main branch on November 17, 2026.

## 5. Dataset Engineering Verification

**Assigned Member:** مشهور رامي مشهور أبو سنينة

**Branch:** Mashhour-Rami

**Pull Request:** [PR #1](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/1)

### Verified Commit Identifiers

| Commit | Description |
|---|---|
| 028cd82 | Implement dataset acquisition and data cleaning |
| 09b4c74 | Remove duplicate acquisition script |
| 3f5bd20 | Implement dataset acquisition and data cleaning |
| 0bf6f40 | Merge commit |

### Technical Deliverables

- [Dataset acquisition script](../../Step_03_Preprocessing/download_dataset.py)
- [Dataset preparation report](../../Step_03_Preprocessing/dataset/dataset_report.json)

### Recorded Results

- 171,332 examined records.
- 42,383 rejected records.
- 128,949 valid candidate records.
- 1,000 selected documents.

**Component Verification:** Passed.

**Individual Authorship:** Requires supporting evidence.

## 6. NLP Preprocessing Verification

**Assigned Member:** عمر عبد الباسط محمود عطية

**Branch:** omar-atiyeh

**Pull Request:** [PR #2](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/2)

### Verified Commit Identifiers

| Commit | Description |
|---|---|
| 644b7e9 | Implement NLP text preprocessing and validation |
| b007807 | Merge commit |

### Technical Deliverables

- [Preprocessing implementation](../../Step_03_Preprocessing/preprocessing.py)
- [Preprocessing results](../../Step_03_Preprocessing/preprocessing_results.txt)

### Validated Functionality

- Text normalization.
- Lowercasing.
- Tokenization.
- Stopword removal.
- Porter Stemming.
- Shared preprocessing interfaces.

**Component Verification:** Passed.

**Individual Authorship:** Requires supporting evidence.

## 7. Inverted Index Verification

**Assigned Member:** ليث بسام محمود جابر

**Branch:** Laith-Jaber

**Pull Request:** [PR #3](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/3)

### Verified Commit Identifiers

| Commit | Description |
|---|---|
| 62b8468 | Component file upload |
| 1e0ccdd | Merge commit |

### Technical Deliverables

- [Inverted index implementation](../../Step_04_Boolean_Search/inverted_index.py)
- [Inverted index results](../../Step_04_Boolean_Search/index_results.txt)

### Recorded Results

| Metric | Value |
|---|---:|
| Indexed Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Total Postings | 87,381 |

**Component Verification:** Passed.

**Individual Authorship:** Requires supporting evidence.

## 8. Boolean Retrieval Verification

**Assigned Member:** محمد مثنى محمد خالد صالح

**Branch:** Mohammad-Saleh

**Pull Request:** [PR #4](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/4)

### Verified Commit Identifiers

| Commit | Description |
|---|---|
| d722afe | Component file upload |
| 693b7ca | Merge commit |

### Technical Deliverables

- [Boolean retrieval implementation](../../Step_04_Boolean_Search/boolean_search.py)
- [Boolean search results](../../Step_04_Boolean_Search/boolean_results.txt)

### Recorded Results

| Query | Matches |
|---|---:|
| covid AND vaccine | 21 |
| covid OR vaccine | 357 |
| NOT vaccine | 923 |
| covid AND NOT vaccine | 280 |
| (covid OR virus) AND vaccine | 53 |

**Component Verification:** Passed.

**Individual Authorship:** Requires supporting evidence.

## 9. Ranked Retrieval and Integration Verification

**Assigned Member:** محمد بهجت فهمي علي

**Branch:** Mohammed-Ali

**Pull Request:** [PR #5](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/5)

### Verified Commit Identifiers

| Commit | Description |
|---|---|
| b9ed99d | Implement TF-IDF ranked retrieval and cosine similarity |
| 587320b | Merge commit |

### Technical Deliverables

- [Ranked retrieval implementation](../../Step_05_Ranked_Search/ranked_search.py)
- [Ranked retrieval results](../../Step_05_Ranked_Search/ranking_results.txt)
- [Unified application](../../Integration/main.py)
- [Integration results](../../Integration/integration_results.txt)
- [Automated system tests](../../Testing/test_system.py)
- [Actual test results](../../Testing/test_results.txt)

### Recorded Results

| Metric | Value |
|---|---:|
| Documents | 1,000 |
| TF-IDF Vocabulary | 10,758 |
| Nonzero TF-IDF Weights | 87,381 |
| Demonstrated Ranked Queries | 3 |
| Automated System Tests Passed | 15/15 |

**Component Verification:** Passed.

**Repository Management and Merge Activity:** Verified.

## 10. Centralized Repository Management

The five verified pull requests were created and merged through the GitHub account:

`MOHAMMEDALMAHSERE`

The repository follows a centralized integration approach managed through the team leader's account.

The verified records establish that:

- Five component-based development branches were used.
- Five pull requests were created.
- Seven commits were included across the five pull requests.
- Five merge commits integrated the corresponding changes.
- All five pull requests were successfully merged into the main branch.
- All assigned technical components are represented within the project.

These records demonstrate repository organization and integration activity.

However, the account responsible for uploading or merging source code is not necessarily the original author of every implementation file.

GitHub pull request records alone cannot establish the independent authorship of all five assigned members.

## 11. Technical Verification Summary

| Verification Area | Result |
|---|---|
| Public Repository Accessibility | Verified |
| Development Branches | 5/5 Verified |
| Pull Requests | 5/5 Verified |
| Successful Merge Status | 5/5 Verified |
| Merge Commit Identifiers | 5/5 Verified |
| Technical Components | Completed |
| Integrated System Demonstration | Passed |
| Automated System Tests | 15/15 Passed |
| Repository Management Activity | Verified |
| Independent Individual Authorship | Additional Evidence Required |

## 12. Supporting Technical Evidence

| Evidence | Location |
|---|---|
| Dataset Preparation | [Dataset Report](../../Step_03_Preprocessing/dataset/dataset_report.json) |
| NLP Preprocessing | [Preprocessing Results](../../Step_03_Preprocessing/preprocessing_results.txt) |
| Inverted Index | [Index Results](../../Step_04_Boolean_Search/index_results.txt) |
| Boolean Retrieval | [Boolean Results](../../Step_04_Boolean_Search/boolean_results.txt) |
| Ranked Retrieval | [Ranking Results](../../Step_05_Ranked_Search/ranking_results.txt) |
| System Integration | [Integration Results](../../Integration/integration_results.txt) |
| Automated Testing | [Test Results](../../Testing/test_results.txt) |

## 13. Individual Contribution Confirmation

Each team member should confirm their actual contribution through an authentic record containing:

- Full name.
- Assigned technical component.
- Specific work personally performed.
- Relevant original implementation files.
- Tests or demonstrations personally executed.
- Supporting communication or development evidence.
- Confirmation date.

Individual confirmations should reflect actual participation and should not be completed on behalf of another member.

## 14. Verification Sources

- [Main Repository](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9)
- [Dataset Pull Request](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/1)
- [NLP Pull Request](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/2)
- [Inverted Index Pull Request](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/3)
- [Boolean Retrieval Pull Request](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/4)
- [Ranked Retrieval Pull Request](https://github.com/MOHAMMEDALMAHSERE/Medical-Research-Search-version9/pull/5)

## 15. Final Verification Statement

The repository development structure, five pull requests, development branch names, merge commits, and successful integration status were verified directly through GitHub.

The Medical Research Search system has successfully completed its core technical implementation, integration demonstration, and all 15 automated system tests.

The available evidence establishes technical completion and centralized repository management.

Independent individual contribution attribution remains subject to authentic supporting records and confirmation by the corresponding team members.

---

**Medical Research Search**

Al al-Bayt University

Information Retrieval Systems — Phase 1

Verification Date: November 17, 2026
