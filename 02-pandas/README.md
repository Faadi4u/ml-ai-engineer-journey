# Pandas — Data Foundations

A structured, hands-on learning section for Pandas, following the Pandas scope in the Python-First ML / AI Engineer Roadmap.

The objective is to become confident at manipulating and cleaning tabular data so it can be used in later data analysis and machine-learning workflows.

## Learning outcomes

By completing this section, you should be able to:

- create and reason about Pandas `Series` and `DataFrame` objects;
- select columns, rows, and individual values;
- filter records using Boolean conditions;
- group records and calculate summaries;
- combine related tables with merge and join operations;
- detect and handle missing values appropriately;
- sort rows and indexes;
- use `map` and `apply` for transformations, while preferring vectorized operations when suitable; and
- work with basic date/time data and time-based summaries.

## Scope

This section intentionally covers only the Pandas concepts listed in the roadmap:

1. Series and DataFrame
2. Selection
3. Filtering
4. GroupBy
5. Merge and join
6. Missing values
7. Sorting
8. Apply and map
9. Time-series basics


## Folder structure

```text
03-pandas/
├── README.md
├── requirements.txt
├── 01-series-dataframe/
│   ├── README.md
│   └── series_dataframe.py
├── 02-selection/
│   ├── README.md
│   └── selection.py
├── 03-filtering/
│   ├── README.md
│   └── filtering.py
├── 04-groupby/
│   ├── README.md
│   └── groupby.py
├── 05-merge-join/
│   ├── README.md
│   └── merge_join.py
├── 06-missing-values/
│   ├── README.md
│   └── missing_values.py
├── 07-sorting/
│   ├── README.md
│   └── sorting.py
├── 08-apply-map/
│   ├── README.md
│   └── apply_map.py
├── 09-time-series/
│   ├── README.md
│   └── time_series.py
└── mini-project/
    ├── README.md
    ├── PROJECT_SPEC.md
    ├── data/
    │   ├── raw/.gitkeep
    │   └── processed/.gitkeep
    ├── reports/.gitkeep
    ├── src/.gitkeep
    └── tests/.gitkeep
```

## How to study each folder

For every topic:

1. Read that folder's `README.md`.
2. Run its Python example from the repository root.
3. Trace the output and explain why it is produced.
4. Complete the exercises in the README.
5. Add your own concise notes or useful edge cases to the README when you discover them.
6. Commit after completing a meaningful topic, rather than after every tiny edit.

Run an example from the learning repository root with:

```bash
python 03-pandas/01-series-dataframe/series_dataframe.py
```

Change the folder and script name for the next topic.

## Progress checklist

- [ ] 01 — Series and DataFrame
- [ ] 02 — Selection
- [ ] 03 — Filtering
- [ ] 04 — GroupBy
- [ ] 05 — Merge and join
- [ ] 06 — Missing values
- [ ] 07 — Sorting
- [ ] 08 — Apply and map
- [ ] 09 — Time-series basics
- [ ] Complete the Pandas data-preparation mini-project