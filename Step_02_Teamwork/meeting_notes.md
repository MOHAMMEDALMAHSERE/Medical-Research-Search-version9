# Team Coordination and Meeting Notes

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| University | Al al-Bayt University |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Members |
| Submission Deadline | November 18, 2026 |
| Last Updated | November 17, 2026 |

---

## 2. Purpose

This document maintains a record of project coordination topics, technical decisions, assigned responsibilities, development checkpoints, and remaining action items.

The coordination process focuses on maintaining compatibility between the independently assigned information retrieval components and ensuring that project requirements are addressed.

The following records summarize documented project decisions and development checkpoints. They are not presented as authenticated meeting transcripts or verified attendance records.

---

## 3. Team Members

| Team Member | Assigned Responsibility |
|---|---|
| محمد بهجت فهمي علي | Team Leadership, Ranked Retrieval, Integration and Testing |
| مشهور رامي مشهور أبو سنينة | Dataset Engineering |
| عمر عبد الباسط محمود عطية | NLP Preprocessing |
| ليث بسام محمود جابر | Inverted Index |
| محمد مثنى محمد خالد صالح | Boolean Retrieval |

---

## 4. Coordination Objectives

- Establish clear project requirements.
- Distribute technical responsibilities.
- Define component inputs and outputs.
- Maintain consistent development practices.
- Monitor technical progress.
- Identify implementation challenges.
- Coordinate component integration.
- Review actual execution results.
- Validate completed deliverables.
- Prepare final presentation and submission materials.

---

## 5. Coordination Record 01 — Project Planning

**Related Stages:** Step 01 and Step 02

### Coordination Topics

- Project problem definition.
- Medical research information retrieval.
- Selection of retrieval algorithms.
- Dataset requirements.
- Team responsibilities.
- Repository organization.
- Phase 1 assessment requirements.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-01 | Develop a medical research information retrieval system. |
| DEC-02 | Use Python as the primary programming language. |
| DEC-03 | Implement Boolean and ranked retrieval. |
| DEC-04 | Divide the project into five technical responsibilities. |
| DEC-05 | Use GitHub for repository management. |
| DEC-06 | Maintain separate technical documentation for each project stage. |
| DEC-07 | Use a command-line interface for Phase 1. |

### Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Prepare project proposal | Team Leader | Completed |
| Organize repository structure | Team Leader | Completed |
| Define technical roles | Team Leader | Completed |
| Establish development milestones | Team Leader | Completed |

### Supporting Documentation

- [Project Proposal](../Step_01_Proposal/)
- [Task Allocation](task_allocation.md)
- [Project Milestones](milestones.md)

---

## 6. Coordination Record 02 — Dataset and NLP Preparation

**Related Stage:** Step 03

### Coordination Topics

- Selection of a suitable research corpus.
- Dataset structure.
- Required document fields.
- Missing-value handling.
- Duplicate detection.
- Document selection strategy.
- Shared text preprocessing.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-08 | Use the BEIR TREC-COVID research corpus. |
| DEC-09 | Prepare a collection of 1,000 valid documents. |
| DEC-10 | Use a fixed random seed of 42 for reproducible selection. |
| DEC-11 | Store prepared documents in CSV format. |
| DEC-12 | Use unique document identifiers. |
| DEC-13 | Apply shared normalization and tokenization. |
| DEC-14 | Apply configurable stopword removal. |
| DEC-15 | Use Porter Stemming. |
| DEC-16 | Reuse the same preprocessing implementation across retrieval components. |

### Agreed Dataset Interface

```text
document_id, title, text, source
```

### Shared Preprocessing Interface

```python
terms = preprocess(text)
processed_text = normalized(text)
```

### Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Acquire research corpus | Mashhour Rami | Component Completed |
| Clean and validate dataset | Mashhour Rami | Component Completed |
| Generate dataset report | Mashhour Rami | Component Completed |
| Implement preprocessing | Omar Atiyeh | Component Completed |
| Demonstrate preprocessing results | Omar Atiyeh | Component Completed |
| Verify shared dependencies | Team Leader | Completed |

### Recorded Technical Outcomes

| Metric | Result |
|---|---:|
| Examined Records | 171,332 |
| Valid Candidate Records | 128,949 |
| Rejected Records | 42,383 |
| Selected Documents | 1,000 |

### Supporting Documentation

- [Dataset and Preprocessing](../Step_03_Preprocessing/)
- [Dataset Report](../Step_03_Preprocessing/dataset/dataset_report.json)
- [Preprocessing Results](../Step_03_Preprocessing/preprocessing_results.txt)

---

## 7. Coordination Record 03 — Inverted Index and Boolean Retrieval

**Related Stage:** Step 04

### Coordination Topics

- Inverted index representation.
- Document posting sets.
- Boolean query processing.
- Operator precedence.
- Unknown search terms.
- Invalid query handling.
- Complete document universe for NOT operations.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-17 | Use Python dictionaries for inverted indexing. |
| DEC-18 | Use sets to represent document postings. |
| DEC-19 | Implement AND using set intersection. |
| DEC-20 | Implement OR using set union. |
| DEC-21 | Implement NOT using set complement. |
| DEC-22 | Support parentheses and logical operator precedence. |
| DEC-23 | Return matching document identifiers. |
| DEC-24 | Validate retrieval using actual research documents. |

### Component Interfaces

```python
index = build_inverted_index(documents)

results = boolean_search(query, index, all_ids)
```

### Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Construct inverted index | Laith Jaber | Component Completed |
| Generate posting statistics | Laith Jaber | Component Completed |
| Implement Boolean operators | Mohammad Saleh | Component Completed |
| Implement expression evaluation | Mohammad Saleh | Component Completed |
| Validate logical retrieval | Mohammad Saleh | Component Completed |
| Verify module compatibility | Team Leader | Completed |

### Recorded Technical Outcomes

| Metric | Result |
|---|---:|
| Indexed Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Total Postings | 87,381 |

### Boolean Demonstration Results

| Query | Matching Documents |
|---|---:|
| covid AND vaccine | 21 |
| covid OR vaccine | 357 |
| NOT vaccine | 923 |
| covid AND NOT vaccine | 280 |
| (covid OR virus) AND vaccine | 53 |

### Supporting Documentation

- [Boolean Search and Inverted Index](../Step_04_Boolean_Search/)
- [Index Results](../Step_04_Boolean_Search/index_results.txt)
- [Boolean Results](../Step_04_Boolean_Search/boolean_results.txt)

---

## 8. Coordination Record 04 — Ranked Information Retrieval

**Related Stage:** Step 05

### Coordination Topics

- Vector Space Model.
- TF-IDF document representation.
- Query vectorization.
- Cosine similarity.
- Top-K retrieval.
- Ranking explanations.
- Consistency with the inverted index vocabulary.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-25 | Use TF-IDF for document and query representation. |
| DEC-26 | Use cosine similarity for document ranking. |
| DEC-27 | Fit the vectorizer on the document collection. |
| DEC-28 | Reuse the fitted vectorizer for subsequent queries. |
| DEC-29 | Store document vectors using sparse matrices. |
| DEC-30 | Support configurable Top-K retrieval. |
| DEC-31 | Display shared term contributions for the highest-ranked result. |
| DEC-32 | Demonstrate at least three real search queries. |

### Ranked Retrieval Interface

```python
ranker = RankedSearch(documents)
results = ranker.search(query, top_k=5)
```

### Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Implement TF-IDF vectorization | Team Leader | Completed |
| Implement cosine similarity | Team Leader | Completed |
| Implement ranked retrieval | Team Leader | Completed |
| Generate ranking explanations | Team Leader | Completed |
| Execute retrieval demonstrations | Team Leader | Completed |
| Execute component self-tests | Team Leader | Completed |

### Recorded Technical Outcomes

| Metric | Result |
|---|---:|
| Documents | 1,000 |
| Vocabulary Terms | 10,758 |
| Nonzero TF-IDF Weights | 87,381 |
| Demonstration Queries | 3 |
| Results per Query | 5 |

### Supporting Documentation

- [Ranked Retrieval](../Step_05_Ranked_Search/)
- [Ranking Results](../Step_05_Ranked_Search/ranking_results.txt)

---

## 9. Coordination Record 05 — System Integration

**Recorded Development Checkpoint:** November 17, 2026

### Coordination Topics

- Integration of all technical modules.
- Shared dataset location.
- Automatic module imports.
- Consistent preprocessing.
- Centralized application execution.
- Unicode terminal output.
- Retrieval regression consistency.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-33 | Use Integration/main.py as the application entry point. |
| DEC-34 | Retain separate component implementations. |
| DEC-35 | Configure module paths automatically. |
| DEC-36 | Use project-relative dataset paths. |
| DEC-37 | Initialize retrieval representations for reuse across queries. |
| DEC-38 | Provide a unified command-line interface. |
| DEC-39 | Support full integrated demonstrations. |
| DEC-40 | Compare integrated results against standalone results. |

### Technical Challenges

| Challenge | Implemented Resolution |
|---|---|
| Separate module directories | Automatic module path configuration |
| Dataset path dependencies | Project-relative file paths |
| Potential preprocessing differences | Shared preprocessing functions |
| Windows Unicode errors | UTF-8 execution configuration |
| Potential ranking inconsistencies | Regression validation |

### Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Integrate dataset loading | Team Leader | Completed |
| Integrate shared preprocessing | Team Leader | Completed |
| Integrate Boolean retrieval | Team Leader | Completed |
| Integrate ranked retrieval | Team Leader | Completed |
| Implement unified interface | Team Leader | Completed |
| Execute integrated demonstration | Team Leader | Passed |

### Recorded Outcome

The unified application successfully reproduced the five Boolean retrieval demonstrations and three ranked retrieval demonstrations.

```text
Demo completed successfully.
```

### Supporting Documentation

- [Integration Documentation](../Integration/)
- [Integration Results](../Integration/integration_results.txt)
- [Integration Log](integration_log.md)

---

## 10. Coordination Record 06 — System Testing and Quality Assurance

**Recorded Development Checkpoint:** November 17, 2026

### Coordination Topics

- Automated system testing.
- Synthetic test collections.
- Real corpus validation.
- Error handling.
- Edge cases.
- Boolean regression.
- Ranked retrieval regression.
- Portable application execution.

### Recorded Project Decisions

| Decision ID | Decision |
|---|---|
| DEC-41 | Use Python unittest for automated testing. |
| DEC-42 | Combine synthetic tests with real corpus tests. |
| DEC-43 | Validate dataset integrity. |
| DEC-44 | Verify index and TF-IDF consistency. |
| DEC-45 | Validate previously recorded retrieval results. |
| DEC-46 | Test invalid inputs and application behavior. |
| DEC-47 | Preserve authentic execution logs as technical evidence. |

### Actual Test Results

| Metric | First Execution | Second Execution |
|---|---:|---:|
| Total Tests | 15 | 15 |
| Passed | 15 | 15 |
| Failed | 0 | 0 |
| Errors | 0 | 0 |
| Execution Time | 10.161s | 8.257s |

### Final Recorded Output

```text
----------------------------------------------------------------------
Ran 15 tests in 8.257s

OK
```

### Outcome

The integrated system passed all 15 automated tests across two executions.

The test pass rate describes functional validation rather than retrieval relevance accuracy.

### Supporting Documentation

- [System Testing](../Testing/)
- [Actual Test Results](../Testing/test_results.txt)

---

## 11. Coordination Record 07 — Final Documentation and Submission Preparation

**Recorded Development Checkpoint:** November 17, 2026

### Coordination Topics

- Completion of technical documentation.
- Repository organization.
- Team contribution evidence.
- Final presentation structure.
- Submission requirements.
- Academic integrity.
- Final verification.

### Recorded and Planned Decisions

| Decision ID | Decision | Status |
|---|---|---|
| DEC-48 | Maintain a comprehensive main README. | Implemented |
| DEC-49 | Preserve actual execution evidence. | Implemented |
| DEC-50 | Maintain dedicated documentation for each project stage. | Implemented |
| DEC-51 | Organize final teamwork documentation. | In Progress |
| DEC-52 | Prepare individual presentation responsibilities. | Planned |
| DEC-53 | Keep the presentation within the required duration. | Planned |
| DEC-54 | Verify the final submission package. | Pending |
| DEC-55 | Submit the required materials before the deadline. | Pending |

### Remaining Action Items

| Action | Assigned Responsibility | Status |
|---|---|---|
| Finalize teamwork documentation | Team Leader | In Progress |
| Verify individual contribution evidence | Entire Team | Pending |
| Prepare individual presentation scripts | Entire Team | Pending |
| Record presentation video | Entire Team | Pending |
| Review submission requirements | Team Leader | Pending |
| Verify final repository accessibility | Team Leader | Pending |
| Complete final submission | Entire Team | Pending |

---

## 12. Planned Presentation Coordination

| Team Member | Presentation Topic | Target Duration |
|---|---|---|
| Mohammed Ali | Project overview, ranked retrieval, integration and testing | Approximately 2 minutes |
| Mashhour Rami | Dataset acquisition and preparation | Approximately 2 minutes |
| Omar Atiyeh | NLP preprocessing | Approximately 2 minutes |
| Laith Jaber | Inverted index construction | Approximately 2 minutes |
| Mohammad Saleh | Boolean retrieval | Approximately 2 minutes |

**Maximum Target Duration:** 10 minutes, including transitions.

The presentation plan has not yet been recorded or submitted.

---

## 13. Actual Meeting Record Template

This template may be used to document verified team meetings.

| Field | Information |
|---|---|
| Meeting ID | To be recorded |
| Date | Actual meeting date |
| Time | Actual meeting time |
| Communication Platform | Actual platform used |
| Attendees | Confirmed participants |
| Agenda | Actual discussion topics |
| Decisions | Confirmed decisions |
| Assigned Actions | Actual assigned tasks |
| Supporting Evidence | Available authentic meeting evidence |

Actual meeting attendance, duration, communication platforms, and individual statements should be added only when supported by genuine records.

---

## 14. Final Coordination Status

| Area | Status |
|---|---|
| Project Planning | Completed |
| Technical Task Allocation | Established |
| Dataset Engineering | Completed |
| NLP Preprocessing | Completed |
| Inverted Index | Completed |
| Boolean Retrieval | Completed |
| Ranked Retrieval | Completed |
| System Integration | Completed |
| Automated System Testing | 15/15 Passed |
| Technical Documentation | Completed |
| Final Teamwork Documentation | In Progress |
| Individual Contribution Verification | Pending |
| Presentation Recording | Pending |
| Final Submission | Pending |

---

## 15. Evidence and Academic Integrity

This document records the project's technical decisions, assigned responsibilities, development outcomes, and planned coordination activities.

The recorded technical results are supported by actual execution evidence.

Coordination records should not be interpreted as independently verified formal meetings, attendance records, or individual authorship claims.

No fabricated meeting dates, attendance details, working hours, or communication transcripts are included.

AI assistance was used to support technical implementation, debugging, testing, and documentation.

---

## 16. Related Documentation

- [Team Contributions](contributions.md)
- [Task Allocation](task_allocation.md)
- [Project Progress Log](progress_log.md)
- [Project Milestones](milestones.md)
- [Development Workflow](development_workflow.md)
- [Integration Log](integration_log.md)
- [Collaboration Evidence](evidence/)
- [Main Repository](../README.md)
- [Final Submission](../Final_Submission/)

---

**Medical Research Search**

Al al-Bayt University

Information Retrieval Systems — Phase 1

Last Updated: November 17, 2026
