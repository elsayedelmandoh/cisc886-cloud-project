"""define typed settings and default configuration values."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = DATA_DIR / "models"
PREDICTIONS_DIR = DATA_DIR / "predictions"

AWS_CONFIG = {
    "region": os.getenv("REGION", "us-east-1"),
    "bucket_name": os.getenv("BUCKET_NAME", "25xrvl-s3"),
    "net_id": os.getenv("NET_ID", "25xrvl"),
    "vpc_cidr": os.getenv("VPC_CIDR", "10.0.0.0/16"),
    "public_subnet_cidr": os.getenv("PUBLIC_SUBNET_CIDR", "10.0.1.0/24"),
    "private_subnet_cidr": os.getenv("PRIVATE_SUBNET_CIDR", "10.0.2.0/24"),
    "emr_subnet_cidr": os.getenv("EMR_SUBNET_CIDR", "10.0.3.0/24"),
}

EC2_CONFIG = {
    "instance_type": os.getenv("EC2_INSTANCE_TYPE", "g4dn.xlarge"),
    "ami": os.getenv("EC2_AMI", "Deep Learning AMI (Ubuntu 20.04)"),
    "storage_gb": int(os.getenv("EC2_STORAGE_GB", "100")),
    "volume_type": os.getenv("EC2_VOLUME_TYPE", "gp3"),
}

EMR_CONFIG = {
    "cluster_name": os.getenv("EMR_CLUSTER_NAME", "25xrvl-emr-cluster"),
    "instance_type": os.getenv("EMR_INSTANCE_TYPE", "m5.xlarge"),
    "num_core_nodes": int(os.getenv("EMR_NUM_CORE_NODES", "2")),
    "release": os.getenv("EMR_RELEASE", "emr-7.2.0"),
    "applications": ["Spark", "Hadoop", "JupyterEnterpriseGateway"],
}

MODEL_CONFIG = {
    "name": os.getenv("MODEL_NAME", "TinyLlama-1.1B-Chat-v1.0"),
    "model_id": os.getenv("MODEL_ID", "TinyLlama/TinyLlama-1.1B-Chat-v1.0"),
    "max_seq_length": int(os.getenv("MODEL_MAX_SEQ_LENGTH", "2048")),
    "load_in_4bit": os.getenv("MODEL_LOAD_IN_4BIT", "true").lower() == "true",
    "lora_r": int(os.getenv("MODEL_LORA_R", "16")),
    "lora_alpha": int(os.getenv("MODEL_LORA_ALPHA", "16")),
    "lora_dropout": int(os.getenv("MODEL_LORA_DROPOUT", "0")),
    "learning_rate": float(os.getenv("MODEL_LEARNING_RATE", "2e-4")),
    "batch_size": int(os.getenv("MODEL_BATCH_SIZE", "2")),
    "epochs": int(os.getenv("MODEL_EPOCHS", "3")),
    "gradient_checkpointing": os.getenv("MODEL_GRADIENT_CHECKPOINTING", "unsloth"),
    "random_seed": int(os.getenv("MODEL_RANDOM_SEED", "3407")),
}

DATASET_CONFIG = {
    "name": os.getenv("DATASET_NAME", "bigcode/the-stack-smol"),
    "dataset_id": os.getenv("DATASET_ID", "bigcode/the-stack-v2-train-smol-ids"),
    "languages": ["python", "javascript", "java", "go"],
    "min_content_length": int(os.getenv("DATASET_MIN_CONTENT_LENGTH", "50")),
    "train_split": float(os.getenv("DATASET_TRAIN_SPLIT", "0.8")),
    "val_split": float(os.getenv("DATASET_VAL_SPLIT", "0.1")),
    "test_split": float(os.getenv("DATASET_TEST_SPLIT", "0.1")),
}

bucket_name = os.getenv("BUCKET_NAME", "25xrvl-s3")
S3_PATHS = {
    "raw": f"s3://{bucket_name}/smol_ids_data/",
    "processed_train": f"s3://{bucket_name}/processed/train/",
    "processed_val": f"s3://{bucket_name}/processed/val/",
    "processed_test": f"s3://{bucket_name}/processed/test/",
    "models": f"s3://{bucket_name}/models/",
}

OLLAMA_CONFIG = {
    "port": int(os.getenv("OLLAMA_PORT", "11434")),
    "api_base": os.getenv("OLLAMA_API_BASE", "http://localhost:11434"),
    "model_name": os.getenv("OLLAMA_MODEL_NAME", "25xrvl-codegpt"),
}

OPENWEBUI_CONFIG = {
    "port": int(os.getenv("OPENWEBUI_PORT", "3000")),
    "url": os.getenv("OPENWEBUI_URL", "http://localhost:3000"),
}

HF_TOKEN = os.getenv("HF_TOKEN", "")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN", "")
REGION = os.getenv("REGION", "us-east-1")
BUCKET_NAME = os.getenv("BUCKET_NAME", "25xrvl-s3")
REPO_ID = os.getenv("REPO_ID", "bigcode/the-stack-v2-train-smol-ids")