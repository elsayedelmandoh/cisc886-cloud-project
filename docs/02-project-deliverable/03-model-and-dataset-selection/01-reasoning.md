# section 3: model & dataset selection (3 marks)

## model selection

| Attribute | Value |
|-----------|-------|
| Model Name | TinyLlama-1.1B-Chat-v1.0 |
| Parameters | 1.1 billion |
| Source | Hugging Face |
| Link | https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 |
| License | Apache 2.0 |

## why tinyllama

1. **Size**: 1.1B parameters fits within 16GB VRAM with 4-bit quantization
2. **Hardware**: Feasible for fine-tuning on Colab + deployment on g4dn.xlarge
3. **Domain Fit**: Pre-trained on 30% code data (Starcoderdata)
4. **Training Data**: Uses Slimpajama + Starcoderdata
5. **Efficiency**: Unsloth provides 2-4x faster training
6. **Chat Capability**: Has instruction tuning

## dataset selection

| Attribute | Value |
|-----------|-------|
| Dataset Name | bigcode/the-stack-v2-train-smol-ids |
| Source | S3 (parquet files) |
| Format | Parquet |
| S3 Location | s3://25xrvl-s3/smol_ids_data/ |

### languages selected

- Python
- JavaScript
- Go

### data leakage avoidance

1. No overlapping commits across splits (by hexsha)
2. Random shuffle before split with fixed seed
3. No data from same repository in train and test