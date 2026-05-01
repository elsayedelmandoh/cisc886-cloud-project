"""shared helper functions used across the project."""

import json
import os
import subprocess
from pathlib import Path
from typing import Any

import boto3
import pandas as pd
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

os.environ["AWS_ACCESS_KEY_ID"] = os.getenv("AWS_ACCESS_KEY_ID", "")
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv("AWS_SECRET_ACCESS_KEY", "")
os.environ["AWS_SESSION_TOKEN"] = os.getenv("AWS_SESSION_TOKEN", "")
os.environ["AWS_DEFAULT_REGION"] = os.getenv("AWS_DEFAULT_REGION", "us-east-1")


def get_s3_client():
    """Create and return an S3 client."""
    return boto3.client("s3")


def upload_file_to_s3(file_path: str, bucket: str, s3_key: str) -> bool:
    """Upload a file to S3 bucket."""
    s3_client = get_s3_client()
    try:
        s3_client.upload_file(file_path, bucket, s3_key)
        print(f"Uploaded {file_path} to s3://{bucket}/{s3_key}")
        return True
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False


def download_file_from_s3(bucket: str, s3_key: str, local_path: str) -> bool:
    """Download a file from S3 bucket."""
    s3_client = get_s3_client()
    try:
        s3_client.download_file(bucket, s3_key, local_path)
        print(f"Downloaded s3://{bucket}/{s3_key} to {local_path}")
        return True
    except ClientError as e:
        print(f"Error downloading file: {e}")
        return False


def list_s3_objects(bucket: str, prefix: str = "") -> list:
    """List all objects in an S3 bucket with given prefix."""
    s3_client = get_s3_client()
    try:
        response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
        if "Contents" in response:
            return [obj["Key"] for obj in response["Contents"]]
        return []
    except ClientError as e:
        print(f"Error listing objects: {e}")
        return []


def create_directory(path: str) -> None:
    """Create a directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def load_json(file_path: str) -> dict:
    """Load JSON from a file."""
    with open(file_path, "r") as f:
        return json.load(f)


def save_json(data: dict, file_path: str) -> None:
    """Save data to a JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=2)


def run_shell_command(command: str, check: bool = True) -> tuple:
    """Run a shell command and return output."""
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )
    if check and result.returncode != 0:
        print(f"Command failed: {command}")
        print(f"Error: {result.stderr}")
    return result.stdout, result.stderr, result.returncode


def download_model_from_huggingface(model_id: str, output_dir: str) -> bool:
    """Download model files from Hugging Face."""
    from huggingface_hub import snapshot_download
    try:
        snapshot_download(
            repo_id=model_id,
            local_dir=output_dir,
            token=os.getenv("HF_TOKEN"),
        )
        print(f"Downloaded model {model_id} to {output_dir}")
        return True
    except Exception as e:
        print(f"Error downloading model: {e}")
        return False


def upload_directory_to_s3(local_dir: str, bucket: str, s3_prefix: str) -> bool:
    """Upload an entire directory to S3."""
    s3_client = get_s3_client()
    local_path = Path(local_dir)
    try:
        for file_path in local_path.rglob("*"):
            if file_path.is_file():
                rel_path = file_path.relative_to(local_path)
                s3_key = f"{s3_prefix}/{rel_path}"
                s3_client.upload_file(str(file_path), bucket, s3_key)
                print(f"Uploaded {file_path} to s3://{bucket}/{s3_key}")
        return True
    except Exception as e:
        print(f"Error uploading directory: {e}")
        return False


def download_directory_from_s3(bucket: str, s3_prefix: str, local_dir: str) -> bool:
    """Download an entire directory from S3."""
    s3_client = get_s3_client()
    create_directory(local_dir)
    try:
        objects = list_s3_objects(bucket, s3_prefix)
        for s3_key in objects:
            if not s3_key.endswith("/"):
                rel_path = s3_key.replace(s3_prefix, "").lstrip("/")
                local_file = Path(local_dir) / rel_path
                local_file.parent.mkdir(parents=True, exist_ok=True)
                s3_client.download_file(bucket, s3_key, str(local_file))
                print(f"Downloaded s3://{bucket}/{s3_key} to {local_file}")
        return True
    except Exception as e:
        print(f"Error downloading directory: {e}")
        return False


def filter_dataset_by_language(df: pd.DataFrame, languages: list) -> pd.DataFrame:
    """Filter dataset by specified languages."""
    return df[df["language"].isin(languages)]


def filter_by_content_length(df: pd.DataFrame, min_length: int) -> pd.DataFrame:
    """Filter dataset by minimum content length."""
    return df[df["content"].str.len() >= min_length]


def filter_by_license(df: pd.DataFrame) -> pd.DataFrame:
    """Filter dataset to only include rows with valid license."""
    return df[df["license"].notna()]


def get_data_statistics(df: pd.DataFrame) -> dict:
    """Calculate statistics for the dataset."""
    stats = {
        "total_samples": len(df),
        "samples_per_language": df["language"].value_counts().to_dict(),
        "avg_content_length": df["content"].str.len().mean(),
        "min_content_length": df["content"].str.len().min(),
        "max_content_length": df["content"].str.len().max(),
    }
    return stats


def train_val_test_split(
    df: pd.DataFrame,
    train_ratio: float = 0.8,
    val_ratio: float = 0.1,
    test_ratio: float = 0.1,
    seed: int = 42,
) -> tuple:
    """Split dataframe into train, validation, and test sets."""
    assert abs(train_ratio + val_ratio + test_ratio - 1.0) < 1e-6
    df_shuffled = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    train_size = int(len(df) * train_ratio)
    val_size = int(len(df) * val_ratio)
    train_df = df_shuffled[:train_size]
    val_df = df_shuffled[train_size : train_size + val_size]
    test_df = df_shuffled[train_size + val_size :]
    return train_df, val_df, test_df


def print_banner():
    """Print project banner."""
    print("=" * 60)
    print("Cloud-Based Conversational Chatbot - CISC 886")
    print("=" * 60)
    print()


def print_config(aws_config, ec2_config, model_config, emr_config):
    """Print current configuration."""
    print_banner()
    print("Configuration:")
    print("-" * 40)
    print(f"AWS Region: {aws_config['region']}")
    print(f"S3 Bucket: {aws_config['bucket_name']}")
    print(f"Net ID: {aws_config['net_id']}")
    print(f"EC2 Instance: {ec2_config['instance_type']}")
    print(f"Model: {model_config['name']}")
    print(f"EMR Cluster: {emr_config['cluster_name']}")
    print()


def run_notebook(path_str: str):
    """Run a specific notebook."""
    import subprocess
    from pathlib import Path
    notebook_path = Path(path_str)
    print(f"Opening notebook: {notebook_path}")
    try:
        subprocess.run(["jupyter", "notebook", str(notebook_path)])
    except FileNotFoundError:
        print("Error: Jupyter not found. Install with: pip install jupyter")


def run_all_notebooks(notebook_dir: str):
    """Launch Jupyter for all notebooks."""
    import subprocess
    from pathlib import Path
    path = Path(notebook_dir)
    print(f"Opening notebook directory: {path}")
    try:
        subprocess.run(["jupyter", "notebook", str(path)])
    except FileNotFoundError:
        print("Error: Jupyter not found. Install with: pip install jupyter")


def list_s3_files(bucket_name: str, prefix: str = ""):
    """List files in S3 bucket."""
    files = list_s3_objects(bucket_name, prefix)
    for f in files:
        print(f"  {f}")


def test_s3_connection():
    """Test S3 connection."""
    s3 = get_s3_client()
    try:
        response = s3.list_buckets()
        print("S3 buckets:")
        for bucket in response.get('Buckets', []):
            print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error: {e}")


def show_help():
    """Show help message."""
    print_banner()
    print("Usage: python app.py [command]")
    print()
    print("Commands:")
    print("  config                    Show current configuration")
    print("  notebook <section>        Open section notebook (1-7)")
    print("  notebooks                 Open all notebooks")
    print("  s3-list                   List files in S3 bucket")
    print("  s3-test                   Test S3 connection")
    print("  help                      Show this help message")
    print()
    print("Sections:")
    print("  1 - System Architecture")
    print("  2 - VPC & Networking")
    print("  3 - Model & Dataset Selection")
    print("  4 - Data Preprocessing with EMR")
    print("  5 - Model Fine-tuning")
    print("  6 - Model Deployment on EC2")
    print("  7 - Web Interface")


def create_spark_session(app_name: str = "cloud-queens", s3_config: dict = None):
    """Create and configure Spark session with S3 support."""
    from pyspark.sql import SparkSession
    
    builder = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "200") \
        .config("spark.default.parallelism", "200") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4")
    
    if s3_config:
        builder = builder \
            .config("spark.hadoop.fs.s3a.access.key", s3_config.get("access_key", "")) \
            .config("spark.hadoop.fs.s3a.secret.key", s3_config.get("secret_key", "")) \
            .config("spark.hadoop.fs.s3a.endpoint", f"s3.{s3_config.get('region', 'us-east-1')}.amazonaws.com")
    
    spark = builder.getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    return spark


def load_data_from_s3(spark, s3_path: str):
    """Load data from S3 (parquet format) using PySpark."""
    print(f"Loading data from: {s3_path}")
    df = spark.read.parquet(s3_path)
    print(f"Loaded {df.count():,} records")
    return df


def filter_by_languages(df, languages: list):
    """Filter DataFrame by target languages."""
    from pyspark.sql.functions import col
    return df.filter(col("language").isin(languages))


def filter_by_content_length(df, min_length: int = 50):
    """Filter DataFrame by minimum content length."""
    from pyspark.sql.functions import col, length
    return df.filter(length(col("content")) > min_length)


def filter_by_license_spark(df):
    """Filter DataFrame to only include rows with valid license."""
    from pyspark.sql.functions import col
    return df.filter(col("license").isNotNull())


def deduplicate_by_hexsha(df):
    """Remove duplicates by hexsha to avoid data leakage."""
    return df.dropDuplicates(["hexsha"])


def split_train_val_test(df, train_ratio: float = 0.8, seed: int = 42):
    """Split DataFrame into train/val/test (80/10/10)."""
    from pyspark.sql.functions import rand, col
    
    df_with_rand = df.withColumn("rand_col", rand(seed))
    
    train_df = df_with_rand.filter(col("rand_col") < train_ratio)
    temp_df = df_with_rand.filter(col("rand_col") >= train_ratio)
    
    val_ratio = (1 - train_ratio) / 2
    val_df = temp_df.filter(col("rand_col") < (train_ratio + val_ratio))
    test_df = temp_df.filter(col("rand_col") >= (train_ratio + val_ratio))
    
    return train_df, val_df, test_df


def save_to_s3(df, s3_path: str, format: str = "json"):
    """Save DataFrame to S3."""
    if format == "json":
        df.write.mode("overwrite").json(s3_path)
    elif format == "parquet":
        df.write.mode("overwrite").parquet(s3_path)
    print(f"Saved to: {s3_path}")


def preprocess_data_spark(spark, input_path: str, output_base: str, config: dict):
    """Full preprocessing pipeline using PySpark."""
    from pyspark.sql.functions import col
    
    print("=" * 60)
    print("STARTING PREPROCESSING PIPELINE")
    print("=" * 60)
    
    # Load
    df = load_data_from_s3(spark, input_path)
    
    # Filter by languages
    languages = config.get("languages", ["python", "javascript", "java", "go"])
    df = filter_by_languages(df, languages)
    print(f"After language filter: {df.count():,}")
    
    # Filter by content length
    min_length = config.get("min_content_length", 50)
    df = filter_by_content_length(df, min_length)
    print(f"After content length filter: {df.count():,}")
    
    # Filter by license
    df = filter_by_license_spark(df)
    print(f"After license filter: {df.count():,}")
    
    # Deduplicate
    df = deduplicate_by_hexsha(df)
    print(f"After deduplication: {df.count():,}")
    
    # Split
    train_df, val_df, test_df = split_train_val_test(df, seed=config.get("seed", 42))
    print(f"Train: {train_df.count():,}")
    print(f"Val: {val_df.count():,}")
    print(f"Test: {test_df.count():,}")
    
    # Save
    save_to_s3(train_df, f"{output_base}/train/", "json")
    save_to_s3(val_df, f"{output_base}/val/", "json")
    save_to_s3(test_df, f"{output_base}/test/", "json")
    
    print("=" * 60)
    print("PREPROCESSING COMPLETE")
    print("=" * 60)