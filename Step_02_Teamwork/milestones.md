# Project Milestones and Development Plan

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| Course | Information Retrieval Systems (902333) |
| University | Al al-Bayt University |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Students |
| Development Methodology | Incremental and Parallel Development |
| Version Control | Git and GitHub |
| Approximate Project Start | November 12, 2026 |
| Target Completion Date | November 17, 2026 |
| Final Submission Date | November 18, 2026 |

## 2. Milestone Overview

| ID | Milestone | Responsible Member | Target Date | Status |
|---|---|---|---|---|
| M01 | Preliminary Research and Planning | Team Leader | Nov 12–15 | In Progress |
| M02 | Repository Setup | Team Leader | Nov 16 | Completed |
| M03 | Problem Definition and Proposal | Team Leader | Nov 16 | Completed |
| M04 | Team Organization and Planning | Team Leader | Nov 16 | In Progress |
| M05 | Dataset Acquisition and Cleaning | Mashhour Rami | Nov 17 | Planned |
| M06 | NLP and Text Preprocessing | Omar Atiyeh | Nov 17 | Planned |
| M07 | Inverted Index Construction | Laith Jaber | Nov 17 | Planned |
| M08 | Boolean Search Implementation | Mohammad Saleh | Nov 17 | Planned |
| M09 | TF-IDF and Ranked Search | Team Leader | Nov 17 | Planned |
| M10 | System Integration | Team Leader | Nov 17 | Planned |
| M11 | Testing and Validation | All Members | Nov 17 | Planned |
| M12 | Documentation and Recorded Presentation | All Members | Nov 17 | Planned |
| M13 | Final Project Submission | Team Leader | Nov 18 | Planned |

## 3. Milestone Details

### M01 — Preliminary Research and Planning

**Owner:** Team Leader

**Approximate Start Date:** November 12, 2026.

**Scope:**

- Preliminary investigation of the project requirements.
- Research into available biomedical datasets.
- Investigation of traditional information retrieval techniques.
- Preliminary system architecture planning.
- Technical preparation for project implementation.

**Expected Outcome:**

Establish a clear understanding of the project requirements, technical components, and proposed implementation approach.

**Target Period:** November 12–15, 2026.

**Status:** In Progress — preliminary activities and their completion will be documented according to available evidence.

### M02 — Repository Setup

**Owner:** Team Leader

**Deliverables:**

- GitHub repository creation.
- Initial README and .gitignore.
- Organized project directory structure.
- Individual development branches.
- Initial Git commits.

**Target Date:** November 16, 2026.

**Status:** Completed.

### M03 — Problem Definition and Proposal

**Owner:** Team Leader

**Deliverables:**

- Problem statement.
- Target users and information needs.
- Project objectives.
- Expected search features.
- Dataset description and acquisition plan.
- Team roles and responsibilities.
- Proposed system architecture.
- Final Phase 1 project proposal.

**Target Date:** November 16, 2026.

**Status:** Completed.

### M04 — Team Organization and Planning

**Owner:** Team Leader

**Deliverables:**

- Individual module ownership.
- Task allocation.
- Project milestones.
- GitHub development workflow.
- Contribution tracking.
- Progress and integration logs.
- Module acceptance criteria.
- Development schedule.

**Target Date:** November 16, 2026.

**Status:** In Progress.

### M05 — Dataset Acquisition and Cleaning

**Owner:** Mashhour Rami

**Branch:** `mashhour-rami`

**Development Section:** `Step_03_Preprocessing/`

**Deliverables:**

- Dataset acquisition script.
- Reproducible sampling configuration.
- Clean document collection.
- Unique document identifiers.
- Structured CSV dataset.
- Dataset statistics and cleaning report.

**Completion Criteria:**

- Target of 1,000 valid documents.
- Minimum of 100 distinct searchable documents.
- No missing required fields or exact duplicates.
- Reproducible dataset preparation.
- Documented dataset source and licensing considerations.
- Valid and consistent document structure.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M06 — NLP and Text Preprocessing

**Owner:** Omar Atiyeh

**Branch:** `omar-atiyeh`

**Development Section:** `Step_03_Preprocessing/`

**Deliverables:**

- Text normalization and lowercasing.
- Tokenization.
- Configurable stopword handling.
- Stemming or lemmatization.
- Reusable preprocessing pipeline.
- Before-and-after preprocessing examples.

**Completion Criteria:**

- Consistent document and query preprocessing.
- Functional and reusable preprocessing module.
- Successful preprocessing tests.
- Documented processing results.
- Safe handling of empty text.
- Configurable preprocessing options.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M07 — Inverted Index Construction

**Owner:** Laith Jaber

**Branch:** `laith-jaber`

**Development Section:** `Step_04_Boolean_Search/`

**Deliverables:**

- Inverted index implementation.
- Python dictionary and set structures.
- Posting lists.
- Term-to-document ID mapping.
- Document metadata retrieval.
- Index demonstration and validation.

**Completion Criteria:**

- Correct term-to-document mapping.
- Valid posting lists.
- Complete indexed document ID set.
- No duplicate document identifiers in posting lists.
- Support for unknown search terms.
- Successful index construction tests.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M08 — Boolean Search Implementation

**Owner:** Mohammad Saleh

**Branch:** `mohammad-saleh`

**Development Section:** `Step_04_Boolean_Search/`

**Deliverables:**

- Boolean query parser.
- AND operator.
- OR operator.
- NOT operator.
- Exact-match document retrieval.
- Matching document IDs and titles.
- Boolean search test results.

**Completion Criteria:**

- Correct implementation of all three Boolean operators.
- AND implemented using set intersection.
- OR implemented using set union.
- NOT evaluated against the complete indexed document collection.
- At least one successful query for each operator.
- Safe handling of empty and invalid queries.
- Dynamically generated search results.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M09 — TF-IDF and Ranked Search

**Owner:** Team Leader

**Development Section:** `Step_05_Ranked_Search/`

**Deliverables:**

- TF-IDF document representation.
- Fitted TF-IDF vectorizer.
- Query vector transformation.
- Vector Space Model implementation.
- Cosine similarity computation.
- Descending document ranking.
- Configurable Top-K retrieval.

**Completion Criteria:**

- Vectorizer fitted on the document collection.
- Queries transformed without refitting.
- Correct cosine similarity computation.
- Documents ranked in descending similarity order.
- Document IDs, titles, and similarity scores displayed.
- At least three ranked search demonstrations.
- Explanation of the highest-ranked results.
- Safe handling of empty and unknown-term queries.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M10 — System Integration

**Owner:** Team Leader

**Development Section:** `Integration/`

**Deliverables:**

- Integrated dataset pipeline.
- Shared preprocessing module.
- Integrated inverted index.
- Integrated Boolean retrieval.
- Integrated ranked retrieval.
- Functional Python console interface.
- Main application entry point.
- Dependency management.

**Completion Criteria:**

- All modules function together.
- Both retrieval methods use the same document collection.
- Search results are generated dynamically.
- Consistent preprocessing across retrieval methods.
- No disconnected or incompatible components.
- Successful execution of the integrated application.
- Documented installation and execution commands.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M11 — Testing and Validation

**Owners:** All Team Members

**Coordinator:** Team Leader

**Development Section:** `Testing/`

**Deliverables:**

- Individual module tests.
- Integration tests.
- Dataset quality validation.
- Preprocessing validation.
- Inverted index validation.
- Boolean search validation.
- Ranked search validation.
- Empty and invalid query tests.
- Reproducible test evidence.

**Completion Criteria:**

- Successful execution of required functionality.
- Documented actual test results.
- Correct and reproducible search outputs.
- Resolution of critical implementation issues.
- Verification of Phase 1 technical requirements.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M12 — Documentation and Recorded Presentation

**Owners:** All Team Members

**Coordinator:** Team Leader

**Development Section:** `Final_Submission/`

**Deliverables:**

- Final project README.
- Installation and execution instructions.
- Individual contribution records.
- Project progress evidence.
- Search demonstration results.
- Academic references.
- External code and AI assistance disclosure.
- Recorded Phase 1 presentation.
- Completed submission checklist.

**Completion Criteria:**

- All Phase 1 requirements reviewed.
- Final integrated system successfully executed.
- All members able to explain their individual contributions.
- Recorded presentation not exceeding 10 minutes.
- Approximately two minutes of explanation per team member.
- Submission materials prepared and verified.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M13 — Final Project Submission

**Owner:** Team Leader

**Deliverables:**

- Final integrated source code.
- Complete GitHub repository.
- Final project proposal.
- Contribution and progress documentation.
- Actual testing evidence.
- Recorded presentation.
- Verified submission requirements.

**Completion Criteria:**

- All required project components are available.
- Repository documentation and navigation are functional.
- Final system execution has been verified.
- Submission materials are ready.
- Project submitted according to the instructor's instructions.

**Target Date:** November 18, 2026.

**Status:** Planned.

## 4. Project Development Schedule

The project was initiated around November 12, 2026, with preliminary project preparation.

The initial preparation period preceded the formal organization of the current GitHub repository.

Development follows an incremental and parallel approach, with the objective of completing all technical, testing, and documentation requirements by November 17, 2026.

| Date | Development Activities | Responsible Members |
|---|---|---|
| November 12, 2026 | Approximate project initiation and preliminary preparation | Team Leader |
| November 13–15, 2026 | Preliminary research and technical planning period | Team Leader |
| November 16, 2026 | GitHub repository setup and organization | Team Leader |
| November 16, 2026 | Problem definition and project proposal | Team Leader |
| November 16, 2026 | Team organization and task allocation | Team Leader |
| November 16–17, 2026 | Dataset acquisition and cleaning | Mashhour Rami |
| November 16–17, 2026 | NLP and text preprocessing | Omar Atiyeh |
| November 16–17, 2026 | Inverted index construction | Laith Jaber |
| November 16–17, 2026 | Boolean search implementation | Mohammad Saleh |
| November 16–17, 2026 | TF-IDF and ranked search | Team Leader |
| November 17, 2026 | Individual module testing | All Members |
| November 17, 2026 | Pull requests and code reviews | Team Leader and All Members |
| November 17, 2026 | System integration | Team Leader |
| November 17, 2026 | Final testing and issue resolution | All Members |
| November 17, 2026 | Final documentation and recorded presentation | All Members |
| November 18, 2026 | Final project submission | Team Leader |

### Key Project Dates

| Milestone | Target Date |
|---|---|
| Approximate Project Initiation | November 12, 2026 |
| Preliminary Preparation Period | November 12–15, 2026 |
| Repository Organization | November 16, 2026 |
| Team Planning Completion | November 16, 2026 |
| Individual Module Completion | November 17, 2026 |
| System Integration | November 17, 2026 |
| Final Testing and Validation | November 17, 2026 |
| Documentation and Presentation | November 17, 2026 |
| Complete Project Readiness | November 17, 2026 |
| Final Submission | November 18, 2026 |

Independent modules may be developed in parallel using small test fixtures before integration with the real dataset.

All implementation, integration, testing, documentation, and presentation activities are targeted for completion by November 17, 2026.

November 18, 2026, is reserved for final submission.

The preliminary project initiation date is approximate. Actual implementation dates and individual contributions will be documented through GitHub commits, pull requests, progress logs, and available development evidence.

## 5. Milestone Dependencies

| Milestone | Dependencies |
|---|---|
| M01 — Preliminary Research | None |
| M02 — Repository Setup | M01 |
| M03 — Project Proposal | M02 |
| M04 — Team Planning | M03 |
| M05 — Dataset Engineering | M04 |
| M06 — Text Preprocessing | M04 |
| M07 — Inverted Index | M04 |
| M08 — Boolean Search | M04 |
| M09 — Ranked Search | M04 |
| M10 — System Integration | M05, M06, M07, M08, M09 |
| M11 — Testing and Validation | M10 |
| M12 — Documentation and Presentation | M11 |
| M13 — Final Submission | M12 |

Component development may begin independently using predefined interfaces and test fixtures.

Final module acceptance requires compatible inputs, outputs, and successful verification of the relevant dependencies.

### Technical Dependencies

| Module | Required Dependencies |
|---|---|
| Dataset Engineering | Original TREC-COVID corpus |
| Text Preprocessing | Valid document text |
| Inverted Index | Document identifiers and processed terms |
| Boolean Search | Inverted index and query preprocessing |
| Ranked Search | Prepared documents and text preprocessing |
| System Integration | All implemented modules |
| Final Validation | Integrated system |

## 6. Progress Tracking Policy

Each milestone will use one of the following statuses:

| Status | Description |
|---|---|
| Planned | The task has been assigned but implementation has not started |
| In Progress | Implementation is currently underway |
| Under Review | Implementation is ready for technical review |
| Completed | The required deliverables and acceptance criteria have been satisfied |
| Blocked | Progress is prevented by an unresolved issue or dependency |

A technical milestone will be marked as completed only after implementation, testing, documentation, code review, and successful integration where applicable.

The team leader will monitor milestone progress, coordinate task completion, review technical contributions, and update development priorities when necessary.

## 7. Academic Evidence

Actual milestone completion will be supported by:

- Dated Git commit history.
- Individual GitHub contributions.
- Development branches.
- Pull requests.
- Code review records.
- Progress notes.
- Individual module test results.
- Integration evidence.
- Final system execution results.

Planned activities must not be reported as completed without supporting evidence.

Individual contributions will be attributed to the members who actually performed the work.

Preliminary activities conducted outside the current GitHub repository will be documented separately when supporting evidence is available.

## 8. Risk Management

| Potential Risk | Mitigation Strategy |
|---|---|
| Limited development time | Parallel module implementation |
| Dataset download failure | Alternative dataset acquisition method |
| Missing or invalid dataset records | Data cleaning and validation |
| Module incompatibility | Standardized inputs and outputs |
| Git merge conflicts | Separate branches and controlled pull requests |
| Incorrect Boolean search results | Operator-specific testing |
| Incorrect ranking results | TF-IDF and cosine similarity validation |
| Delayed module completion | Continuous progress monitoring |
| Missing documentation | Documentation alongside implementation |
| Integration failure | Incremental integration and module-level testing |
| Submission delay | Complete all deliverables before the submission date |

## 9. Development Status

Project preparation began around November 12, 2026.

Repository organization and project proposal documentation have been completed.

Team organization and development planning are currently in progress.

All assigned technical modules are scheduled for parallel implementation under the coordination of the team leader.

The target is to complete the integrated Information Retrieval System, testing activities, documentation, and recorded presentation by November 17, 2026.

Final project submission is scheduled for November 18, 2026.

Actual progress, individual contributions, and milestone completion will be updated throughout development.

---

**Medical Research Search**

Information Retrieval Systems (902333)

Al al-Bayt University — Phase 1
