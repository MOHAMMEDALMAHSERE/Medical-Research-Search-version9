# Dataset Description and Acquisition Plan

## 1. Dataset Overview

The Medical Research Search project will use the TREC-COVID dataset provided through the BEIR benchmark.

TREC-COVID is designed for biomedical information retrieval and contains scientific literature related to COVID-19 and coronavirus research.

| Property | Description |
|---|---|
| Dataset Name | TREC-COVID |
| Benchmark | BEIR |
| Domain | Biomedical Information Retrieval |
| Language | English |
| Original Corpus Size | 171,332 documents |
| Available Queries | 50 |
| Original Format | Parquet |
| Target Collection Size | 1,000 documents |
| Project Output Format | CSV |
| Listed Dataset License | CC BY-SA 4.0 |

## 2. Dataset Sources

- Dataset: https://huggingface.co/datasets/BeIR/trec-covid
- BEIR Benchmark: https://beir.ai
- TREC-COVID Official Website: https://ir.nist.gov/trec-covid/
- CORD-19 License: https://github.com/allenai/cord19/blob/master/LICENSE
- BEIR Research Paper: https://arxiv.org/abs/2104.08663

## 3. Dataset Selection Justification

TREC-COVID was selected because:

- It is a real biomedical research collection.
- It is directly relevant to the project's application domain.
- It provides structured document identifiers, titles, and text.
- It supports traditional information retrieval techniques.
- It contains sufficient documents for reproducible sampling.
- It is recommended in the course project implementation guide.

## 4. Original Dataset Structure

The dataset provides two subsets:

- Corpus: scientific research documents.
- Queries: benchmark search queries.

The corpus subset will be used as the primary document collection for Phase 1.

### Original Fields

| Field | Data Type | Description |
|---|---|---|
| _id | String | Original unique document identifier |
| title | String | Research document title |
| text | String | Research document content |

## 5. Planned Document Schema

The prepared dataset will use the following structure:

| Field | Data Type | Description |
|---|---|---|
| document_id | String | Unique identifier preserved from the original dataset |
| title | String | Document title |
| text | String | Original searchable document content |
| source | String | Dataset provenance |

The source field will identify TREC-COVID as the dataset source. Category and publication date will only be included if reliable metadata is available.

The searchable content will combine the document title and text.

## 6. Dataset Acquisition Plan

The dataset preparation process will include:

1. Download the TREC-COVID corpus.
2. Record the dataset version and source.
3. Validate the required document fields.
4. Remove missing and empty records.
5. Remove records with invalid identifiers.
6. Remove exact duplicate documents.
7. Select 1,000 valid documents using reproducible random sampling.
8. Export the prepared collection as a UTF-8 CSV file.
9. Record dataset statistics and validation results.

## 7. Reproducible Sampling Configuration

| Parameter | Value |
|---|---|
| Target Sample Size | 1,000 |
| Minimum Required Documents | 100 |
| Sampling Method | Random sampling without replacement |
| Random Seed | 42 |
| Missing Text Removal | Enabled |
| Empty Text Removal | Enabled |
| Missing Title Removal | Enabled |
| Duplicate Removal | Enabled |
| Encoding | UTF-8 |

The dataset revision, deterministic record ordering, sampling configuration, and selected document identifiers will be documented to support reproducibility.

## 8. Data Quality Requirements

The final document collection must satisfy the following conditions:

- At least 100 valid and distinct documents.
- Unique document identifiers.
- Non-empty document titles.
- Meaningful searchable English text.
- No exact duplicate records.
- Consistent document structure.
- Valid CSV formatting.

## 9. Planned Dataset Usage

The same prepared document collection will be used for:

- Text preprocessing.
- Inverted index construction.
- Boolean information retrieval.
- TF-IDF document representation.
- Cosine similarity computation.
- Ranked document retrieval.
- System integration and testing.

## 10. Licensing and Academic Usage

The Hugging Face dataset card lists the CC BY-SA 4.0 license.

Because the documents originate from CORD-19 and underlying scientific publications, the project will also respect applicable original source licenses and copyright restrictions.

The dataset will be used for academic information retrieval experiments and educational text mining.

Dataset sources will be properly cited. Raw research content will not be publicly redistributed unless permitted by the applicable licenses.

A reproducible dataset acquisition script and documentation will be provided.

## 11. References

1. Thakur et al. (2021). BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models.
   https://arxiv.org/abs/2104.08663

2. National Institute of Standards and Technology. TREC-COVID.
   https://ir.nist.gov/trec-covid/

3. Hugging Face. BeIR/trec-covid Dataset Card.
   https://huggingface.co/datasets/BeIR/trec-covid

4. Allen Institute for Artificial Intelligence. CORD-19 Dataset License.
   https://github.com/allenai/cord19/blob/master/LICENSE

## 12. Development Status

This document defines the planned dataset acquisition, preparation, and usage process.

Actual dataset statistics, cleaning results, sampling results, and validation evidence will be documented during Step 03 — Dataset and Text Preprocessing.
