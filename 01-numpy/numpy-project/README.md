# ML Data Preprocessing Pipeline (NumPy Core)

A hands-on NumPy capstone that brings together core array operations used in numerical data preparation: reshaping, splitting, Boolean filtering, anomaly detection, copying, feature transformations, aggregation, and linear algebra.

> **Scope:** This is a small educational pipeline using synthetic data. It simulates token IDs and embedding-like numeric vectors; it does not implement a real tokenizer, train a machine-learning model, or produce validated semantic embeddings.

## Project goals

By completing this project, you will practise how to:

- represent structured data with NumPy `ndarray` objects;
- reshape a flat token stream into a matrix and create an 80/20 sentence-level split;
- locate invalid sentinel values and filter valid positive values with Boolean masks;
- protect raw data by working on an independent copy;
- apply `np.log` and scalar scaling through vectorized operations;
- calculate summaries along specific axes; and
- compare rows of a matrix using dot products.

## Pipeline overview

### Task 1 — Token topology and data splitting

Create 60 consecutive integer token IDs beginning at `100`. Reshape them to `(10, 6)`, treating each row as one sentence containing six token IDs. Split by rows into eight training sentences and two testing sentences. Iterate over the test portion and print each row.

Concepts: array creation, `reshape`, `split`, indexing, iteration, `shape`.

### Task 2 — Data cleansing and anomaly removal

Create a one-dimensional array of eight model-weight-like values. Include at least two `-999.0` sentinel values. Find and report their index positions, use a Boolean mask to keep only values that are both non-corrupted and positive, then sort those values in ascending order.

Concepts: Boolean comparisons, Boolean indexing, `np.where`, sorting.

### Task 3 — Memory preservation and feature scaling

Create a raw feature matrix whose values range from `10.0` through `50.0`. Make an independent copy and demonstrate that editing the copy does not change the original. Apply the natural logarithm with `np.log`, then multiply the transformed values by a scalar compression factor using broadcasting.

Concepts: `copy`, memory independence, universal functions (ufuncs), array arithmetic, scalar broadcasting.

**Terminology note:** multiplying by a scalar is scalar scaling; it is not the same as statistical standardization (z-score scaling). This project uses scalar compression because that is the operation specified.

### Task 4 — Embedding-matrix summaries and dot products

Create a synthetic matrix with three profiles and four numeric features, shape `(3, 4)`. Calculate each profile's mean across its four features with `mean(axis=1)`, and calculate the four-feature mean profile with `mean(axis=0)`. Use a matrix dot product between the matrix and its transpose to produce a `(3, 3)` pairwise dot-product matrix.

Concepts: aggregation, `axis`, transpose, `@` or `np.dot`.

**Interpretation note:** `mean(axis=1)` returns three scalar means (one per row); `mean(axis=0)` returns a four-element mean vector across the three rows. The dot-product matrix is a numeric alignment measure, not cosine similarity. Since the inputs are synthetic, it should not be described as validated semantic similarity.

## Requirements

- Python 3.10 or newer recommended
- NumPy

Install NumPy if needed:

```bash
python -m pip install numpy
```

## Run the project

From the directory containing the script, run:

```bash
python numpy_ml_pipeline.py
```

## Suggested project structure

```text
numpy-ml-pipeline/
├── README.md
├── PROJECT_SPEC.md
└── numpy_ml_pipeline.py
```

## Completion checklist

- [ ] Task 1 produces a `(10, 6)` sentence matrix, an `(8, 6)` training matrix, and a `(2, 6)` test matrix.
- [ ] Task 2 reports all sentinel indices and returns only positive, non-corrupted values in ascending order.
- [ ] Task 3 proves that modifying the copy leaves the raw matrix unchanged.
- [ ] Task 3 applies `np.log` and scalar scaling without Python loops.
- [ ] Task 4 reports row means, a four-element feature mean vector, and a `(3, 3)` dot-product matrix.
- [ ] The script runs from top to bottom without errors and labels its output clearly.

## Implementation approach

Build and verify one task at a time. Print array shapes alongside selected outputs so the structural transformations are easy to inspect. Prefer vectorized NumPy operations over explicit Python loops, except where iteration is specifically required in Task 1.
