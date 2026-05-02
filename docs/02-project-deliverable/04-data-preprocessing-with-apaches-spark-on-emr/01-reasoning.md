# section 4: data preprocessing with apache spark on emr (5 marks)

## emr cluster configuration

| Setting | Value |
|---------|-------|
| Cluster Name | 25xrvl-emr-sg |
| Instance Type | m5.xlarge (master), m5.xlarge (core) x2 |
| Number of Nodes | 3 |
| Region | us-east-1 |
| Release | emr-7.2.0 |
| Applications | Spark 3.5, Hadoop 3, JupyterEnterpriseGateway |

## pyspark preprocessing pipeline

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("25xrvl-preprocessing") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load from S3
df = spark.read.json("s3://25xrvl-s3/smol_ids_data/*")

# Filter by target languages
languages = ["python", "javascript", "go"]
df_filtered = df.filter(df["language"].isin(languages))

# Remove empty or very short content
df_filtered = df_filtered.filter(length(df["content"]) > 50)

# Remove ambiguous licenses
df_filtered = df_filtered.filter(df["license"].isNotNull())

# Train/validation/test split (80/10/10)
train_df, val_df, test_df = df_filtered.randomSplit([0.8, 0.1, 0.1], seed=42)

# Save to S3
train_df.write.json("s3://25xrvl-s3/processed/train/")
val_df.write.json("s3://25xrvl-s3/processed/val/")
test_df.write.json("s3://25xrvl-s3/processed/test/")

spark.stop()
```

## required screenshots

- [ ] EMR console screenshot showing cluster configuration
- [ ] EMR console screenshot showing cluster in **Terminated state** (CRITICAL)
- [ ] S3 screenshot showing output files (train/, val/, test/)
- [ ] EDA: Token length distribution histogram
- [ ] EDA: Language distribution chart
- [ ] EDA: Sample count per split chart

> **IMPORTANT**: Teardown screenshot is REQUIRED. EMR clusters left running deplete the shared AWS account.
