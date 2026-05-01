# system architecture and component boundaries

## architecture diagram

```
                                    Internet
                                        |
                                        v
                              +-------------------+
                              |   Internet Gateway|
                              +-------------------+
                                        |
                                        v
                              +-------------------+
                              |   Load Balancer   |
                              +-------------------+
                                        |
                                        v
                              +-------------------+
                              |   EC2 (g4dn.xlarge)|
                              |   + Ollama        |
                              |   + OpenWebUI    |
                              +-------------------+
                                        ^
                                        |
                              +-------------------+
                              |   S3 Bucket       |
                              |   25xrvl-s3-project   |
                              +-------------------+
                                        ^
                                        |
                              +-------------------+
                              |   EMR Cluster     |
                              |   (PySpark)        |
                              +-------------------+
```

## major components

| Component | Purpose | Input | Output |
|-----------|---------|-------|--------|
| S3 Bucket | Store dataset and model | Raw data, fine-tuned GGUF | Processed data, model files |
| EMR Cluster | PySpark preprocessing | Raw dataset from HF | Filtered data by language |
| Colab | Fine-tuning with QLoRA | Filtered dataset | LoRA adapter weights |
| EC2 Instance | Model serving | GGUF model | API responses |
| OpenWebUI | Web interface | User queries | Chat responses |

## where state lives

- **Model weights**: S3 bucket (25xrvl-s3-project)
- **Training data**: S3 preprocessed
- **LoRA adapters**: Saved locally then uploaded
- **Configuration**: AWS tags and environment variables

## failure points

- EMR cluster teardown (must screenshot for grading)
- Colab disconnects during fine-tuning
- EC2 instance capacity unavailable
- GGUF export compatibility issues
