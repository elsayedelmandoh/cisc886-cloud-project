# Colab Setup for Section 5 Fine-tuning

## Prerequisites

1. **Google Account** with Google Colab access
2. **AWS Credentials** from `.env` file
3. **HuggingFace Token** from `.env` file

## Step 1: Upload Notebook to Colab

1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `notebooks/05-model-fine-tuning/01-fine-tuning.ipynb`

## Step 2: Set Up Credentials (Recommended: Colab Secrets)

1. Click the **key icon** (🔐) in the left sidebar → **Add new secret**
2. Add these secrets:

| Secret Name | Value (from .env file) |
|-------------|-----------------------|
| AWS_ACCESS_KEY_ID | (your AWS access key from .env) |
| AWS_SECRET_ACCESS_KEY | (your AWS secret key from .env) |
| HF_TOKEN | (your HuggingFace token from .env) |
| REGION | us-east-1 |
| BUCKET_NAME | 25xrvl-s3 |

The notebook automatically loads these via `os.getenv()` (same pattern as `src/config/settings.py`).

## Step 3: Select GPU

1. Click **Runtime** → **Change runtime type**
2. Select **GPU** (T4 or better)
3. Click **Save**

## Notebook flow:

01. Install packages
02. Imports and configuration
03. Load base model (4-bit)
04. Generate base model outputs (before training)
05. Load processed data from S3 (from Section 4)
06. Setup LoRA (QLoRA)
07. Train for 3 epochs > loss curve
08. Generate fine-tuned outputs
09. Compare base vs fine-tuned
10. Export to GGUF > upload to S3

## Troubleshooting

**Out of Memory**: Reduce batch size or training samples
**S3 Upload Fails**: Verify AWS credentials are correct
**HF Token Issues**: Ensure token has read access to dataset