# Project Specification: ML Data Preprocessing Pipeline (NumPy Core)

## 1. Project overview

Develop a single Python script, `numpy_ml_pipeline.py`, that demonstrates foundational NumPy techniques used when preparing numeric data for machine-learning workflows. The implementation must be divided into four clearly labelled tasks and use synthetic data so that the transformations can be inspected and reproduced.

This is a NumPy learning project, not a production NLP system. It does not tokenize real text, train a model, or create actual language-model embeddings.

## 2. Technical competencies

The finished implementation must demonstrate:

1. `ndarray` creation and shape inspection.
2. Indexing, slicing, and Boolean masks.
3. Vectorized array arithmetic.
4. Broadcasting between compatible shapes, including a scalar and a matrix.
5. The `np.log` universal function.
6. Independent copying and protection of source data.
7. Aggregation along specified axes.
8. Reshaping arrays.
9. Iteration over rows in a selected array.
10. Searching for sentinel values with `np.where` and sorting values.
11. Splitting a dataset along a specified axis.
12. Linear algebra with a dot product.

## 3. Deliverables

Required files:

- `numpy_ml_pipeline.py` — executable implementation of all four tasks.
- `README.md` — project overview, concepts, setup, and usage.
- `PROJECT_SPEC.md` — this specification.

The script must be runnable with `python numpy_ml_pipeline.py` after NumPy is installed.

## 4. Functional requirements

### Task 1 — Token generation, topology, and data splitting

**Scenario:** A simulated tokenizer has produced a flat stream of integer token IDs. The project organizes that stream into sentence-shaped rows and separates training data from testing data.

**Requirements:**

1. Generate 60 consecutive, unique integer values starting at `100` (from `100` through `159`).
2. Reshape the sequence into a two-dimensional array with shape `(10, 6)`. Each row represents one simulated sentence with six token IDs.
3. Split by sentence/row, not by individual token, into an 80/20 partition: eight training rows and two testing rows.
4. The required shapes are:
   - all sentences: `(10, 6)`
   - training sentences: `(8, 6)`
   - testing sentences: `(2, 6)`
5. Iterate over the testing sentences and print each test row.

**Acceptance criteria:** Every ID is unique; the first ID is `100`; the final ID is `159`; no rows are lost or duplicated by the split; the split maintains complete six-token sentences.

### Task 2 — Data cleansing and anomaly removal

**Scenario:** An array of numeric weights contains an invalid sentinel value, `-999.0`, used to indicate corrupted or missing data.

**Requirements:**

1. Define a one-dimensional array containing exactly eight weight-like values.
2. Include at least two occurrences of `-999.0`.
3. Use a programmatic search to identify and store the indices where the sentinel occurs. Report the positions clearly. Note that `np.where(condition)` returns a tuple of index arrays.
4. Build a Boolean mask that retains only values that are both non-corrupted and positive (`> 0`).
5. Use that mask to construct a cleaned array.
6. Sort the cleaned values into ascending order.

**Acceptance criteria:** All sentinel positions are reported; no sentinel or non-positive value remains in the cleaned output; the output is sorted ascending.

### Task 3 — Memory preservation and non-linear feature scaling

**Scenario:** A raw numeric feature matrix must be transformed without accidentally modifying the source matrix.

**Requirements:**

1. Create a two-dimensional numeric matrix with values in the range `10.0` to `50.0` inclusive.
2. Make an independent copy of the raw matrix using a NumPy copy operation. Do not rely on a view or a simple alias.
3. Demonstrate memory independence by changing at least one element in a temporary copy or by otherwise verifying that a copy edit does not modify the raw matrix. Preserve the unmodified raw matrix for later comparison.
4. Apply the natural logarithm to the copied feature values using `np.log`.
5. Multiply the log-transformed matrix by a scalar compression factor. Use NumPy broadcasting to apply the scalar uniformly across the matrix.
6. Print or inspect the raw, copied/transformed, and final scaled arrays clearly enough to verify the transformation.

**Acceptance criteria:** The original matrix remains unchanged after a copy edit; `np.log` is applied to positive values; the scaled matrix has the same shape as the raw matrix; no explicit element-by-element Python loop is needed for the transformation.

**Terminology clarification:** The specified operation is scalar compression after a logarithmic transform. It is not z-score standardization, min-max scaling, or the scikit-learn `StandardScaler` algorithm. A clearly named scalar such as `scale_factor` should be used, and the chosen factor should be explained in a comment.

### Task 4 — Matrix aggregation and profile alignment

**Scenario:** Three synthetic feature profiles are represented as rows in a matrix. The program calculates summaries and pairwise dot products.

**Requirements:**

1. Define a two-dimensional numeric matrix with exactly three rows and four features per row, shape `(3, 4)`.
2. Calculate each row's mean using `mean(axis=1)`. This produces a one-dimensional array of shape `(3,)`, with one scalar mean per profile.
3. Calculate the mean feature vector across all three profiles using `mean(axis=0)`. This produces a one-dimensional array of shape `(4,)`.
4. Calculate the pairwise dot-product matrix using the original matrix and its transpose (for example, `embeddings @ embeddings.T` or the equivalent `np.dot` operation).
5. Confirm the result has shape `(3, 3)` and print it with a clear label.

**Acceptance criteria:** Input shape is `(3, 4)`; row means have shape `(3,)`; the feature-wise mean vector has shape `(4,)`; pairwise dot products have shape `(3, 3)`.

**Interpretation clarification:** The input rows are synthetic numeric profiles, not embeddings generated by an NLP model. Dot products can be described as pairwise dot-product scores or alignment measures, but not as cosine similarity unless the vectors are first normalized. Do not claim that this demonstration proves actual semantic similarity.

## 5. Engineering and presentation requirements

- Import NumPy once at the top of the script.
- Initialize any random generator with an explicit seed if random data is used.
- Separate the four tasks with comments or section headings.
- Use descriptive variable names and print labels for key outputs.
- Inspect and report array shapes at important transformations.
- Prefer vectorized NumPy operations where appropriate.
- The script must run from top to bottom without errors.
- Keep the implementation understandable to a learner who is consolidating NumPy fundamentals.

## 6. Out of scope

The following are not required:

- a real text tokenizer or a real text corpus;
- an actual machine-learning or language model;
- trained embeddings or validated semantic similarity;
- a production data pipeline, deployment, API, or database;
- pandas, scikit-learn, PyTorch, or other libraries beyond NumPy.

## 7. Execution

Install NumPy if it is not already available:

```bash
python -m pip install numpy
```

Run the implementation from its project directory:

```bash
python numpy_ml_pipeline.py
```

The output should be organized by task, with relevant values and shapes visible for review.
