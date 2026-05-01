#!/usr/bin/env python3
"""
Data Preprocessing with PySpark on AWS EMR
Section 4: Data Preprocessing with Apache Spark on EMR

Usage:
    spark-submit --master yarn --deploy-mode cluster src/preprocessing/preprocess_emr.py

Or run locally:
    python src/preprocessing/preprocess_emr.py
"""

import sys
import os

# Add project root to path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.config.settings import (
    AWS_CONFIG,
    DATASET_CONFIG,
    S3_PATHS,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    REGION,
)
from src.utils.helpers import (
    create_spark_session,
    load_data_from_s3,
    filter_by_languages,
    filter_by_content_length,
    filter_by_license_spark,
    deduplicate_by_hexsha,
    split_train_val_test,
    save_to_s3,
)


def main():
    """Main entry point"""
    print("=" * 60)
    print("PYSPARK PREPROCESSING ON EMR")
    print("=" * 60)
    print(f"Bucket: {AWS_CONFIG['bucket_name']}")
    print(f"Region: {AWS_CONFIG['region']}")
    print(f"Languages: {DATASET_CONFIG['languages']}")
    print(f"Min content length: {DATASET_CONFIG['min_content_length']}")
    print()
    
    # S3 paths
    RAW_PATH = S3_PATHS["raw"]
    OUTPUT_TRAIN = S3_PATHS["processed_train"]
    OUTPUT_VAL = S3_PATHS["processed_val"]
    OUTPUT_TEST = S3_PATHS["processed_test"]
    
    # S3 config for Spark
    s3_config = {
        "access_key": AWS_ACCESS_KEY_ID,
        "secret_key": AWS_SECRET_ACCESS_KEY,
        "region": REGION,
    }
    
    # Create Spark session
    spark = create_spark_session(app_name="25xrvl-preprocessing", s3_config=s3_config)
    
    try:
        # Load data from S3
        print("Loading data from S3...")
        df = load_data_from_s3(spark, RAW_PATH)
        
        # Preprocessing config
        preprocess_config = {
            "languages": DATASET_CONFIG["languages"],
            "min_content_length": DATASET_CONFIG["min_content_length"],
            "seed": 42,
        }
        
        # Filter by languages
        print("\nFiltering by languages...")
        df = filter_by_languages(df, preprocess_config["languages"])
        print(f"  After language filter: {df.count():,}")
        
        # Filter by content length
        print("Filtering by content length...")
        df = filter_by_content_length(df, preprocess_config["min_content_length"])
        print(f"  After content length filter: {df.count():,}")
        
        # Filter by license
        print("Filtering by license...")
        df = filter_by_license_spark(df)
        print(f"  After license filter: {df.count():,}")
        
        # Deduplicate
        print("Removing duplicates...")
        df = deduplicate_by_hexsha(df)
        print(f"  After deduplication: {df.count():,}")
        
        # Split into train/val/test (80/10/10)
        print("\nSplitting data (80/10/10)...")
        train_df, val_df, test_df = split_train_val_test(df, seed=preprocess_config["seed"])
        
        train_count = train_df.count()
        val_count = val_df.count()
        test_count = test_df.count()
        
        print(f"  Train: {train_count:,}")
        print(f"  Validation: {val_count:,}")
        print(f"  Test: {test_count:,}")
        
        # Show language distribution
        print("\nLanguage distribution (train):")
        train_df.groupBy("language").count().orderBy("count", ascending=False).show()
        
        # Save to S3
        print("\nSaving to S3...")
        save_to_s3(train_df, OUTPUT_TRAIN, "json")
        save_to_s3(val_df, OUTPUT_VAL, "json")
        save_to_s3(test_df, OUTPUT_TEST, "json")
        
        print("\n" + "=" * 60)
        print("PREPROCESSING COMPLETE!")
        print("=" * 60)
        print(f"Train: {OUTPUT_TRAIN}")
        print(f"Validation: {OUTPUT_VAL}")
        print(f"Test: {OUTPUT_TEST}")
        
    finally:
        print("\nStopping Spark session...")
        spark.stop()


if __name__ == "__main__":
    main()