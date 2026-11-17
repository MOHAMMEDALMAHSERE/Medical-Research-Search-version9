# Phase 1 — Final Submission Checklist

## 1. Project Information

| Property            | Description                            |
| ------------------- | -------------------------------------- |
| Project             | Medical Research Search                |
| University          | Al al-Bayt University                  |
| Course              | Information Retrieval Systems (902333) |
| Phase               | Phase 1                                |
| Team Size           | 5 Members                              |
| Submission Deadline | November 18, 2026                      |
| Last Updated        | November 17, 2026                      |

## 2. Step 01 — Problem Definition and Proposal

**Allocated Marks: 3**

- [x] Define the information retrieval problem.
- [x] Establish the project objectives.
- [x] Identify the target application domain.
- [x] Select a suitable research dataset.
- [x] Define Boolean and ranked retrieval features.
- [x] Document team responsibilities.
- [x] Prepare the project proposal.
- [x] Organize proposal documentation.

**Evidence:** [Step 01 — Proposal](../Step_01_Proposal/)

**Status:** Completed.

## 3. Step 02 — Progress and Teamwork

**Allocated Marks: 3**

- [x] Identify all five team members.
- [x] Define assigned technical responsibilities.
- [x] Establish development milestones.
- [x] Document task allocation.
- [x] Document development workflow.
- [x] Record project progress.
- [x] Map technical deliverables to assigned responsibilities.
- [x] Document component development branches.
- [x] Document five merged pull requests.
- [x] Document integration activities.
- [x] Organize technical execution evidence.
- [x] Document contribution verification limitations.
- [x] Complete teamwork documentation.

**Evidence:**

- [Teamwork Documentation](../Step_02_Teamwork/)
- [Team Contributions](../Step_02_Teamwork/contributions.md)
- [Progress Log](../Step_02_Teamwork/progress_log.md)
- [Evidence Register](../Step_02_Teamwork/evidence/)
- [Contribution Verification Report](../Step_02_Teamwork/evidence/contribution_verification.md)

**Status:** Documentation completed.

**Verification Note:** Repository branches, pull requests, and technical deliverables establish project organization and integration. They do not independently verify every member's authorship.

## 4. Step 03 — Dataset and Text Preprocessing

**Allocated Marks: 3**

- [x] Use a real research document corpus.
- [x] Prepare at least 100 distinct documents.
- [x] Prepare a collection of 1,000 documents.
- [x] Include unique document identifiers.
- [x] Include document titles and text.
- [x] Validate required dataset fields.
- [x] Remove invalid records.
- [x] Detect duplicate identifiers.
- [x] Detect duplicate content.
- [x] Apply text normalization.
- [x] Apply lowercasing.
- [x] Apply tokenization.
- [x] Implement configurable stopword removal.
- [x] Apply Porter Stemming.
- [x] Demonstrate original text and processed terms.
- [x] Record dataset preparation statistics.
- [x] Record actual preprocessing results.
- [ ] Verify the English-language document requirement explicitly.
- [ ] Confirm applicable dataset redistribution permissions.

### Actual Dataset Results

| Metric                  |  Result |
| ----------------------- | ------: |
| Examined Records        | 171,332 |
| Rejected Records        |  42,383 |
| Valid Candidate Records | 128,949 |
| Selected Documents      |   1,000 |
| Random Seed             |      42 |

**Evidence:** [Step 03 — Dataset and Preprocessing](../Step_03_Preprocessing/)

**Status:** Technical implementation completed.

The preprocessing pipeline primarily targets English, although the selected corpus may contain documents or titles in other languages.

## 5. Step 04 — Inverted Index and Boolean Retrieval

**Allocated Marks: 3**

- [x] Construct an inverted index.
- [x] Use Python dictionaries.
- [x] Use sets for document postings.
- [x] Associate processed terms with document identifiers.
- [x] Implement Boolean AND.
- [x] Implement Boolean OR.
- [x] Implement Boolean NOT.
- [x] Use the complete document universe for NOT.
- [x] Support operator precedence.
- [x] Support parentheses.
- [x] Handle invalid Boolean queries.
- [x] Demonstrate search using actual documents.
- [x] Display matching document identifiers and titles.
- [x] Document the difference between Boolean and ranked retrieval.
- [x] Record execution results.

### Actual Index Results

| Metric            | Result |
| ----------------- | -----: |
| Indexed Documents |  1,000 |
| Vocabulary Terms  | 10,758 |
| Total Postings    | 87,381 |

### Actual Boolean Results

| Query                        | Matching Documents |
| ---------------------------- | -----------------: |
| covid AND vaccine            |                 21 |
| covid OR vaccine             |                357 |
| NOT vaccine                  |                923 |
| covid AND NOT vaccine        |                280 |
| (covid OR virus) AND vaccine |                 53 |

**Evidence:** [Step 04 — Boolean Search](../Step_04_Boolean_Search/)

**Status:** Completed.

## 6. Step 05 — TF-IDF and Ranked Retrieval

**Allocated Marks: 4**

- [x] Implement TF-IDF document vectorization.
- [x] Construct a document-term matrix.
- [x] Apply shared preprocessing to queries.
- [x] Reuse the fitted vectorizer.
- [x] Calculate cosine similarity.
- [x] Sort documents by descending similarity.
- [x] Implement configurable Top-K retrieval.
- [x] Display document identifiers.
- [x] Display document titles.
- [x] Display cosine similarity scores.
- [x] Demonstrate at least three search queries.
- [x] Explain the highest-ranked results.
- [x] Validate empty and unknown queries.
- [x] Execute ranked retrieval self-tests.
- [x] Record actual ranking results.

### Actual Ranked Search Results

| Query                               | Highest Score |
| ----------------------------------- | ------------: |
| covid vaccine immune response       |      0.451483 |
| respiratory infection treatment     |      0.331911 |
| coronavirus transmission prevention |      0.279990 |

**Evidence:** [Step 05 — Ranked Search](../Step_05_Ranked_Search/)

**Status:** Completed.

## 7. System Integration

- [x] Integrate all retrieval modules.
- [x] Establish shared dataset loading.
- [x] Integrate NLP preprocessing.
- [x] Integrate inverted index construction.
- [x] Integrate Boolean retrieval.
- [x] Integrate ranked retrieval.
- [x] Implement a unified command-line interface.
- [x] Support custom Top-K.
- [x] Support ranking explanations.
- [x] Configure automatic module imports.
- [x] Support Unicode terminal output.
- [x] Execute the complete system demonstration.
- [x] Verify standalone and integrated result consistency.

**Evidence:** [Integration](../Integration/)

**Status:** Completed.

## 8. Automated System Testing

- [x] Implement automated testing using Python unittest.
- [x] Validate synthetic document collections.
- [x] Validate the real 1,000-document collection.
- [x] Verify dataset integrity.
- [x] Verify preprocessing behavior.
- [x] Verify inverted index construction.
- [x] Verify Boolean query processing.
- [x] Verify ranked retrieval.
- [x] Verify Top-K and similarity score bounds.
- [x] Verify invalid input handling.
- [x] Verify interactive application behavior.
- [x] Verify portable execution.
- [x] Verify Boolean regression results.
- [x] Verify ranked retrieval regression results.
- [x] Save actual execution evidence.

### Final Test Results

| Category          | Passed | Failed |
| ----------------- | -----: | -----: |
| Synthetic Tests   |      9 |      0 |
| Real Corpus Tests |      6 |      0 |
| Total             |     15 |      0 |

Final recorded execution time: 8.257 seconds.

**Evidence:** [Testing](../Testing/)

**Status:** All tests passed.

## 9. Repository and Documentation

- [x] Organize repository directories.
- [x] Complete the main README.
- [x] Complete individual stage documentation.
- [x] Document system architecture.
- [x] Document implementation methods.
- [x] Provide execution instructions.
- [x] Document actual execution results.
- [x] Document technical limitations.
- [x] Acknowledge external sources.
- [x] Acknowledge AI assistance.
- [x] Verify all final documentation links.
- [x] Verify that a clean repository checkout can reproduce the application.
- [x] Confirm final repository accessibility for the instructor.

## 10. Presentation Video

- [x] Define presentation topics.
- [x] Allocate topics to five team members.
- [x] Prepare individual presentation scripts.
- [x] Plan a maximum total duration of 10 minutes.
- [x] Record the five individual presentation sections.
- [x] Include actual application demonstrations.
- [x] Combine the recorded sections.
- [x] Check presentation duration.
- [x] Check audio and video quality.
- [x] Upload the final presentation video.
- [x] Verify video accessibility.
- [x] Add the final presentation URL.

**Evidence:** [Presentation Script](video_script.md)

**Status:** Recording pending.

## 11. Official Submission

- [x] Confirm the instructor's final submission instructions.
- [x] Confirm whether one team member or every member must submit.
- [x] Confirm the required submission platform.
- [x] Confirm whether a repository link alone is sufficient.
- [x] Include the project proposal if required separately.
- [x] Include the presentation video link if required.
- [x] Verify all required files.
- [x] Submit the required materials before the deadline.
- [x] Confirm successful submission.

## 12. Assessment Summary

| Step  | Assessment Area                      | Allocated Marks |
| ----- | ------------------------------------ | --------------: |
| 01    | Problem Definition and Proposal      |               3 |
| 02    | Progress and Teamwork                |               3 |
| 03    | Dataset and Text Preprocessing       |               3 |
| 04    | Inverted Index and Boolean Retrieval |               3 |
| 05    | TF-IDF and Ranked Retrieval          |               4 |
| Total | Phase 1                              |              16 |

The marks listed above are allocated assessment marks, not awarded grades.

## 13. Final Readiness

The core technical implementation, integration, automated testing, and project documentation have been completed.

The remaining activities concern final repository verification, dataset compliance, presentation recording, and official submission.

---

**Medical Research Search**

Phase 1 — Final Submission Checklist
