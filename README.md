# NYC Taxi ETL Pipeline

This repository contains an ETL pipeline for processing the NYC taxi dataset using Databricks Lakeflow Declarative Pipelines.

## Folder Structure

- `explorations/`: Contains notebooks and files for exploratory data analysis.
- `transformations/`: Contains source code for data transformations.
  - `bronze_layer.py`: Raw data ingestion.
  - `silver_layer.py`: Cleaned and enriched data.
  - `gold_layer.py`: Aggregated and business-level data.
- `utilities/`: Contains utility functions and modules.

```text
nyc-taxi-etl-pipeline/
├── explorations/
│   └── exploration_notebook.ipynb
├── transformations/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   └── gold_layer.py
├── utilities/
│   └── utility_functions.py
