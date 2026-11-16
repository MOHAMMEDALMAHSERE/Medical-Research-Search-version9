# GitHub Development Workflow

## 1. Overview

The Medical Research Search project follows an incremental and collaborative development workflow using Git and GitHub.

Each team member is responsible for implementing, testing, and documenting an assigned technical module within an individual development branch.

The team leader coordinates development, reviews technical contributions, manages integration, and maintains the main branch.

## 2. Branching Strategy

| Branch | Owner | Responsibility |
|---|---|---|
| `main` | Team Leader | Stable and integrated project |
| `laith-jaber` | Laith Jaber | Inverted Index |
| `mohammad-saleh` | Mohammad Saleh | Boolean Search |
| `omar-atiyeh` | Omar Atiyeh | NLP and Text Preprocessing |
| `mashhour-rami` | Mashhour Rami | Dataset Engineering and Data Cleaning |

The team leader will also maintain a dedicated development branch for TF-IDF, ranked retrieval, and integration activities.

## 3. Branch Responsibilities

### Main Branch

The main branch represents the approved project version.

It contains:

- Project documentation.
- Reviewed technical modules.
- Approved source code.
- Integrated system components.
- Verified testing evidence.
- Final submission materials.

Technical changes should be reviewed before being merged into the main branch.

### Individual Development Branches

Each team member will use an assigned branch to:

- Implement technical functionality.
- Develop and improve source code.
- Perform individual module testing.
- Document implementation decisions.
- Record actual development progress.
- Prepare contributions for integration.

Team members should avoid modifying components outside their assigned responsibilities without coordination.

## 4. Development Workflow

The following workflow will be used for technical implementation:

1. Review the assigned task and acceptance criteria.
2. Update the individual development branch from the main branch.
3. Implement the assigned module.
4. Perform local testing and validation.
5. Document actual implementation results.
6. Commit changes with descriptive messages.
7. Push changes to the assigned GitHub branch.
8. Create a pull request targeting the main branch.
9. Address technical feedback and requested changes.
10. Receive approval from the team leader.
11. Merge the approved contribution.
12. Verify integration compatibility.

## 5. Git Commit Guidelines

Each commit should represent a meaningful development activity.

Commit messages should clearly describe the implemented change.

### Example Commit Messages

| Module | Example Commit Message |
|---|---|
| Dataset | Add TREC-COVID dataset acquisition script |
| Data Cleaning | Implement duplicate and missing record removal |
| Preprocessing | Implement text normalization and tokenization |
| Preprocessing | Add configurable stopword removal |
| Inverted Index | Implement term-to-document posting lists |
| Boolean Search | Implement AND, OR, and NOT operations |
| Ranked Search | Implement TF-IDF document vectorization |
| Ranked Search | Add cosine similarity and Top-K ranking |
| Testing | Add Boolean search unit tests |
| Integration | Integrate Boolean and ranked retrieval modules |
| Documentation | Document actual module test results |

These messages are examples of planned development activities and do not represent completed contributions.

Each member should commit their own work using their individual GitHub account and correctly configured Git identity.

## 6. Pull Request Requirements

Each pull request should include:

- A descriptive title.
- The purpose of the implemented changes.
- A list of modified or created files.
- A description of implemented functionality.
- Actual testing results.
- Known limitations or unresolved issues.
- References to the assigned task.

### Pull Request Template

**Module:**

Name of the implemented technical module.

**Author:**

Responsible team member.

**Summary:**

Description of the implemented functionality.

**Changes:**

List of completed technical changes.

**Testing:**

Actual tests performed and their results.

**Dependencies:**

Required modules, libraries, or datasets.

**Known Issues:**

Existing limitations or unresolved problems.

## 7. Code Review Process

The team leader will review each technical contribution based on:

- Compliance with project requirements.
- Correctness of the implementation.
- Code readability and organization.
- Compatibility with other modules.
- Appropriate input and output handling.
- Successful testing results.
- Reproducibility.
- Absence of hard-coded search results.
- Appropriate documentation and source attribution.

Contributions requiring improvements will be returned to their owners before integration.

## 8. Merge Strategy

Approved contributions will be merged into the main branch using pull requests.

Merge commits are preferred to preserve individual contribution history.

Before merging, the team leader will verify that:

- The assigned module satisfies its acceptance criteria.
- Required tests have been executed successfully.
- The contribution does not introduce unresolved conflicts.
- The changes are compatible with the project architecture.
- Individual contributions remain correctly attributed.

Merged changes will be recorded in the integration log.

## 9. Module Integration Requirements

All technical modules must follow compatible data structures and interfaces.

The shared document collection will contain:

| Field | Type |
|---|---|
| document_id | String |
| title | String |
| text | String |
| source | String |

Both Boolean and ranked retrieval must use the same prepared document collection.

Text preprocessing must be consistent across document indexing and query processing.

Boolean operators must be preserved during query parsing.

The ranked retrieval module must transform user queries using the previously fitted TF-IDF vectorizer.

## 10. Conflict Management

To minimize development conflicts:

- Each member should modify only their assigned files.
- Shared files require coordination with the team leader.
- Members should regularly synchronize relevant changes.
- Merge conflicts should be resolved before final integration.
- Existing functionality must be tested after conflict resolution.

## 11. Contribution Tracking

Individual contributions will be documented through:

- Git commit history.
- Pull requests.
- Code review records.
- Module implementation files.
- Actual test results.
- Progress logs.
- Integration records.

Branch ownership alone does not constitute evidence of implementation.

Contributions will be attributed to the members who actually performed the work.

## 12. Development Schedule

| Date | Planned Activity |
|---|---|
| November 16, 2026 | Branch organization and technical task assignment |
| November 16–17, 2026 | Parallel module implementation |
| November 17, 2026 | Pull requests and code reviews |
| November 17, 2026 | System integration and validation |
| November 17, 2026 | Final documentation and recorded presentation |
| November 18, 2026 | Final project submission |

## 13. Academic Integrity

All team members must:

- Understand and explain their implemented components.
- Maintain accurate records of their contributions.
- Cite external source code and datasets.
- Disclose relevant AI assistance.
- Report actual testing results.
- Avoid fabricated development evidence.

## 14. Development Status

This document defines the planned collaborative development workflow.

Actual commits, pull requests, code reviews, testing results, and integration activities will be recorded throughout project development.

---

**Medical Research Search**

Information Retrieval Systems (902333)

Al al-Bayt University — Phase 1
