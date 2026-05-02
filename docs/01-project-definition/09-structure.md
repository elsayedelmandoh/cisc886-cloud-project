# repository structure and file responsibilities

## project structure

```text
cisc886-cloud-project/
├── app.py                          # main entry point with cli commands
├── requirements.txt                # python dependencies
├── .env                            # environment variables (secrets)
├── .env.example                    # example environment variables
├── .gitignore                      # git ignore rules
├── license                         # project license
│
├── src/                            # source code modules
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py             # configuration settings and defaults
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py              # shared helper functions
│   │   ├── upload_data_to_s3.py   # s3 upload utilities
│   │   └── pdf_to_md.py           # pdf conversion utilities
│   ├── preprocessing/
│   │   └── preprocess_emr.py      # emr preprocessing scripts
│   └── infrastructure/
│       ├── __init__.py
│       └── main.tf                # terraform infrastructure code
│
├── notebooks/                      # jupyter notebooks (7 sections)
│   ├── 00-quickstart.ipynb
│   ├── 01-system-architecture/
│   ├── 02-vpc-and-networking/
│   ├── 03-model-and-dataset-selection/
│   ├── 04-data-preprocessing-with-apaches-spark-on-emr/
│   ├── 05-model-fine-tuning/
│   ├── 06-model-deployment-on-ec2/
│   └── 07-web-interface/
│
├── data/                           # data directories
│   ├── raw/
│   ├── processed/
│   ├── samples/
│   ├── models/
│   ├── predictions/
│   ├── vectorizers/
│   ├── remote_cache/
│   └── smol_ids_data/             # raw dataset (parquet files)
│
└── docs/                           # documentation
    ├── 00-research/
    ├── 01-project-definition/
    └── 02-project-deliverable/
```

## directory explanation

- app.py: entrypoint for local startup, cli commands, and quick validation.
- src/config: runtime configuration and environment loading (settings.py).
- src/utils: shared utilities for s3 operations, data processing, spark session creation.
- src/preprocessing: emr-specific pyspark preprocessing scripts.
- src/infrastructure: terraform configuration for aws infrastructure.
- notebooks: exploratory and iterative work for each of the 7 project sections.
- tests: unit and integration coverage for critical paths.
- data/raw: source data kept as close to the original form as possible.
- data/processed: cleaned and transformed datasets from emr preprocessing.
- data/samples: small fixture-like datasets for fast iteration.
- data/models: serialized model artifacts and fine-tuned gguf files.
- data/predictions: output predictions and inference results.
- data/vectorizers: fitted text or feature preprocessing artifacts.
- data/remote_cache: downloaded or cached external artifacts.

