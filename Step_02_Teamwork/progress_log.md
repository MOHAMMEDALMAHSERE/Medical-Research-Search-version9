# Project Progress Log

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
| Target Completion | November 17, 2026 |
| Final Submission | November 18, 2026 |
| Last Updated | November 16, 2026 |

## 2. Purpose

This document maintains a chronological record of the development progress of the Medical Research Search system.

The progress log tracks:

- Project development activities.
- Technical decisions.
- Individual contributions.
- Completed milestones.
- Implementation challenges.
- Testing and validation results.
- Code reviews and system integration.
- Remaining development tasks.

## 3. Preliminary Project Preparation

### November 12–15, 2026 — Preliminary Preparation Period

**Responsible Member:** Team Leader

**Phase:** Research and Planning

The project was initiated around November 12, 2026, before the formal organization of the current GitHub repository.

The preliminary preparation involved project planning and technical preparation for the Information Retrieval System.

Detailed activities and supporting evidence from this period will be documented where available.

**Status:** Preliminary preparation reported by the team leader.

## 4. Development Progress

### November 16, 2026 — Repository Setup

**Responsible Member:** Team Leader

**Completed Activities:**

- Created the GitHub repository.
- Organized project development directories.
- Prepared the initial README and .gitignore files.
- Established the main development branch.
- Created the initial project documentation.

**Outcome:**

An organized repository structure was established to support incremental development and team collaboration.

**Evidence:** GitHub repository structure and commit history.

**Status:** Completed.

### November 16, 2026 — Problem Definition and Project Proposal

**Responsible Member:** Team Leader

**Completed Activities:**

- Defined the project problem.
- Identified target users and information needs.
- Defined measurable project objectives.
- Selected the TREC-COVID dataset.
- Documented the dataset acquisition strategy.
- Defined expected Boolean and ranked retrieval features.
- Designed the proposed system architecture.
- Prepared the Phase 1 project proposal.
- Documented team roles and responsibilities.

**Evidence:**

- `Step_01_Proposal/problem_statement.md`
- `Step_01_Proposal/objectives.md`
- `Step_01_Proposal/search_features.md`
- `Step_01_Proposal/dataset_description.md`
- `Step_01_Proposal/team_roles.md`
- `Step_01_Proposal/phase1-proposal.docx`
- `Step_01_Proposal/README.md`

**Status:** Completed.

### November 16, 2026 — Team Organization and Technical Planning

**Responsible Member:** Team Leader

**Activities:**

- Defined individual technical responsibilities.
- Revised task allocation to distribute development activities.
- Established module ownership.
- Defined expected module inputs and outputs.
- Established module acceptance criteria.
- Defined project milestones.
- Established the development schedule.
- Defined the GitHub collaborative development workflow.
- Established individual contribution tracking.
- Prepared the project progress log.

**Evidence:**

- `Step_02_Teamwork/task_allocation.md`
- `Step_02_Teamwork/milestones.md`
- `Step_02_Teamwork/development_workflow.md`
- `Step_02_Teamwork/contributions.md`
- `Step_02_Teamwork/progress_log.md`

**Status:** In Progress.

## 5. Technical Development Tracking

| Module | Responsible Member | Current Status | Target Completion |
|---|---|---|---|
| Dataset Acquisition and Cleaning | Mashhour Rami | Planned | November 17 |
| NLP and Text Preprocessing | Omar Atiyeh | Planned | November 17 |
| Inverted Index | Laith Jaber | Planned | November 17 |
| Boolean Retrieval | Mohammad Saleh | Planned | November 17 |
| TF-IDF and Ranked Retrieval | Team Leader | Planned | November 17 |
| System Integration | Team Leader | Planned | November 17 |
| Testing and Validation | All Members | Planned | November 17 |
| Documentation and Presentation | All Members | Planned | November 17 |
| Final Submission | Team Leader | Planned | November 18 |

## 6. Technical Decision Log

| ID | Decision | Justification |
|---|---|---|
| TD01 | Use Python | Suitable for implementing traditional information retrieval techniques |
| TD02 | Use TREC-COVID | Provides a real biomedical research document collection |
| TD03 | Target 1,000 documents | Provides a manageable collection for Phase 1 |
| TD04 | Use random seed 42 | Supports reproducible dataset sampling |
| TD05 | Use a shared preprocessing pipeline | Ensures consistent document and query processing |
| TD06 | Use Python dictionaries and sets | Supports inverted index and Boolean set operations |
| TD07 | Implement Boolean retrieval | Enables exact logical document matching |
| TD08 | Use TF-IDF | Supports weighted document and query representation |
| TD09 | Use cosine similarity | Enables similarity-based document ranking |
| TD10 | Fit the vectorizer on documents only | Ensures consistent document and query vector spaces |
| TD11 | Use a Python console interface | Satisfies Phase 1 interface requirements |
| TD12 | Use individual development branches | Supports parallel development and contribution tracking |
| TD13 | Use pull requests and code reviews | Supports controlled integration and technical validation |
| TD14 | Complete development by November 17 | Provides preparation time before final submission |
| TD15 | Document dataset acquisition rather than unrestricted redistribution | Supports compliance with applicable dataset licenses |

These decisions represent the approved or proposed technical approach. Their implementation will be verified during development.

## 7. Challenges and Mitigation

| Challenge | Proposed Solution | Status |
|---|---|---|
| Large original dataset | Select a reproducible collection of 1,000 documents | Planned |
| Missing or duplicate documents | Implement dataset validation and cleaning | Planned |
| Limited development time | Develop independent modules in parallel | Planned |
| Module compatibility | Define consistent data structures and interfaces | Planned |
| Git merge conflicts | Use assigned branches and controlled pull requests | Planned |
| Inconsistent text preprocessing | Use a shared preprocessing pipeline | Planned |
| Incorrect Boolean results | Test each Boolean operator independently | Planned |
| Incorrect ranked results | Validate TF-IDF vectors and similarity calculations | Planned |

This table identifies anticipated implementation challenges. It does not represent issues already encountered or resolved.

## 8. November 17 — Planned Development Activities

### Individual Module Implementation

- Mashhour Rami: Dataset acquisition and cleaning.
- Omar Atiyeh: NLP and text preprocessing.
- Laith Jaber: Inverted index construction.
- Mohammad Saleh: Boolean retrieval implementation.
- Team Leader: TF-IDF and ranked retrieval implementation.

### Code Review and Integration

- Review individual technical contributions.
- Verify module inputs and outputs.
- Review pull requests.
- Resolve implementation and compatibility issues.
- Merge approved contributions.
- Integrate all components into a unified application.

### Testing and Validation

- Validate dataset quality.
- Test preprocessing functionality.
- Verify inverted index construction.
- Test AND, OR, and NOT operations.
- Demonstrate at least three ranked search queries.
- Validate cosine similarity scores.
- Test empty and invalid queries.
- Execute the integrated application.

### Final Preparation

- Update individual contribution records.
- Record actual testing evidence.
- Complete project documentation.
- Prepare the recorded presentation.
- Verify the final submission checklist.

**Target Status:** Complete project readiness by November 17, 2026.

**Actual Status:** Pending execution and verification.

## 9. November 18 — Final Submission

**Responsible Member:** Team Leader

**Planned Activities:**

- Verify the final GitHub repository.
- Confirm all required files are available.
- Confirm that execution instructions are correct.
- Verify documentation and presentation materials.
- Submit the project according to the instructor's instructions.

**Status:** Planned.

## 10. Progress Entry Template

The following template will be used to document subsequent development activities.

### Development Entry

- Date:
- Contributor:
- Assigned Module:
- Completed Activity:
- Created or Modified Files:
- Commit Link:
- Pull Request Link:
- Testing Performed:
- Actual Test Results:
- Challenges:
- Next Action:
- Status:

## 11. Progress Verification Policy

Progress records must reflect actual development activities.

Each completed technical activity should be supported by relevant evidence, such as:

- GitHub commits.
- Pull requests.
- Source code changes.
- Actual execution results.
- Testing reports.
- Code review records.
- Integration logs.

Planned activities must not be marked as completed before implementation and verification.

## 12. Current Project Status

The project proposal and repository organization have been completed.

Team management documentation and technical planning are currently in progress.

The technical modules are scheduled for parallel implementation, followed by system integration, testing, documentation, and recorded presentation.

The project completion target is November 17, 2026, with final submission scheduled for November 18, 2026.

This progress log will be updated according to actual development activities.

---

**Medical Research Search**

Information Retrieval Systems (902333)

Al al-Bayt University — Phase 1
