# Project Milestones and Development Plan

## 1. Project Information

| Property | Description |
|---|---|
| Project | Medical Research Search |
| Course | Information Retrieval Systems (902333) |
| Phase | Phase 1 |
| Team Leader | محمد بهجت فهمي علي |
| Team Size | 5 Students |
| Development Methodology | Incremental and Parallel Development |
| Version Control | Git and GitHub |
| Target Completion Date | November 17, 2026 |
| Final Submission Date | November 18, 2026 |

## 2. Milestone Overview

| ID | Milestone | Responsible Member | Target Date | Status |
|---|---|---|---|---|
| M01 | Repository Setup | Team Leader | Nov 16 | Completed |
| M02 | Problem Definition and Proposal | Team Leader | Nov 16 | Completed |
| M03 | Team Organization and Planning | Team Leader | Nov 16 | In Progress |
| M04 | Dataset Acquisition and Cleaning | Mashhour Rami | Nov 17 | Planned |
| M05 | NLP and Text Preprocessing | Omar Atiyeh | Nov 17 | Planned |
| M06 | Inverted Index Construction | Laith Jaber | Nov 17 | Planned |
| M07 | Boolean Search Implementation | Mohammad Saleh | Nov 17 | Planned |
| M08 | TF-IDF and Ranked Search | Team Leader | Nov 17 | Planned |
| M09 | System Integration | Team Leader | Nov 17 | Planned |
| M10 | Testing and Validation | All Members | Nov 17 | Planned |
| M11 | Documentation and Presentation | All Members | Nov 17 | Planned |
| M12 | Final Project Submission | Team Leader | Nov 18 | Planned |

## 3. Milestone Details

### M01 — Repository Setup

**Owner:** Team Leader

**Deliverables:**

- GitHub repository creation.
- Initial README and .gitignore.
- Organized project directory structure.
- Individual development branches.
- Initial Git commits.

**Target Date:** November 16, 2026.

**Status:** Completed.

### M02 — Problem Definition and Proposal

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

### M03 — Team Organization and Planning

**Owner:** Team Leader

**Deliverables:**

- Individual module ownership.
- Task allocation.
- Project milestones.
- GitHub development workflow.
- Contribution tracking.
- Progress and integration logs.
- Module acceptance criteria.

**Target Date:** November 16, 2026.

**Status:** In Progress.

### M04 — Dataset Acquisition and Cleaning

**Owner:** Mashhour Rami

**Branch:** `mashhour-rami`

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

**Target Date:** November 17, 2026.

**Status:** Planned.

### M05 — NLP and Text Preprocessing

**Owner:** Omar Atiyeh

**Branch:** `omar-atiyeh`

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

**Target Date:** November 17, 2026.

**Status:** Planned.

### M06 — Inverted Index Construction

**Owner:** Laith Jaber

**Branch:** `laith-jaber`

**Deliverables:**

- Inverted index implementation.
- Python dictionary and set structures.
- Posting lists.
- Document ID mapping.
- Document metadata retrieval.
- Index demonstration and validation.

**Completion Criteria:**

- Correct term-to-document mapping.
- Valid posting lists.
- Complete indexed document ID set.
- No duplicate document identifiers in posting lists.
- Successful index construction tests.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M07 — Boolean Search Implementation

**Owner:** Mohammad Saleh

**Branch:** `mohammad-saleh`

**Deliverables:**

- Boolean query parser.
- AND operator.
- OR operator.
- NOT operator.
- Matching document IDs and titles.
- Boolean search test results.

**Completion Criteria:**

- Correct implementation of all three Boolean operators.
- NOT evaluated against the complete indexed document collection.
- At least one successful query for each operator.
- Safe handling of empty and invalid queries.
- Dynamically generated search results.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M08 — TF-IDF and Ranked Search

**Owner:** Team Leader

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
- Correct cosine similarity scores and ranking.
- Document IDs, titles, and similarity scores displayed.
- At least three ranked search demonstrations.
- Explanation of the highest-ranked results.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M09 — System Integration

**Owner:** Team Leader

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

**Target Date:** November 17, 2026.

**Status:** Planned.

### M10 — Testing and Validation

**Owners:** All Team Members

**Coordinator:** Team Leader

**Deliverables:**

- Individual module tests.
- Integration tests.
- Dataset quality validation.
- Preprocessing validation.
- Boolean search validation.
- Ranked search validation.
- Empty and invalid query tests.
- Reproducible test evidence.

**Completion Criteria:**

- Successful execution of required functionality.
- Documented actual test results.
- Correct search outputs.
- Resolution of critical implementation issues.
- Verification of Phase 1 technical requirements.

**Target Date:** November 17, 2026.

**Status:** Planned.

### M11 — Documentation and Recorded Presentation

**Owners:** All Team Members

**Coordinator:** Team Leader

**Deliverables:**

- Final project README.
- Installation and execution instructions.
- Individual contribution records.
- Project progress evidence.
- Search demonstration results.
- Academic references and AI assistance disclosure.
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

### M12 — Final Project Submission

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

The project follows an accelerated development schedule based on incremental implementation and parallel collaboration.

| Date | Planned Activities | Responsible Members |
|---|---|---|
| November 16, 2026 | Repository setup and organization | Team Leader |
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

### Key Project Deadlines

| Deadline | Target Date |
|---|---|
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

Actual completion dates will be documented through GitHub commits, pull requests, and progress logs.

## 5. Milestone Dependencies

| Milestone | Dependencies |
|---|---|
| M01 — Repository Setup | None |
| M02 — Project Proposal | M01 |
| M03 — Team Planning | M02 |
| M04 — Dataset Engineering | M03 |
| M05 — Text Preprocessing | M03 |
| M06 — Inverted Index | M03 |
| M07 — Boolean Search | M03 |
| M08 — Ranked Search | M03 |
| M09 — System Integration | M04, M05, M06, M07, M08 |
| M10 — Testing and Validation | M09 |
| M11 — Documentation and Presentation | M10 |
| M12 — Final Submission | M11 |

Component development may begin independently using predefined interfaces and test fixtures.

Final module acceptance requires compatible inputs, outputs, and successful verification of the relevant dependencies.

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

The team leader will monitor milestone progress and coordinate task completion.

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

## 8. Risk Management

| Potential Risk | Mitigation Strategy |
|---|---|
| Limited development time | Parallel module implementation |
| Dataset download failure | Alternative dataset acquisition method |
| Module incompatibility | Standardized inputs and outputs |
| Git merge conflicts | Separate branches and controlled pull requests |
| Incorrect search results | Individual and integration testing |
| Delayed module completion | Continuous progress monitoring |
| Missing documentation | Documentation alongside implementation |

## 9. Development Status

Repository setup and project proposal documentation have been completed.

Team organization and development planning are currently in progress.

All assigned technical modules are scheduled for parallel implementation.

The target is to complete the integrated Information Retrieval System, testing activities, documentation, and recorded presentation by November 17, 2026.

Final project submission is scheduled for November 18, 2026.

Actual progress and milestone completion will be updated throughout development.

---

**Medical Research Search**

Information Retrieval Systems (902333)

Al al-Bayt University — Phase 1
