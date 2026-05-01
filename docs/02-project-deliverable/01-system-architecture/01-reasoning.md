# section 1: system architecture (2 marks)

## diagram reference

The system architecture is shown in the system architecture diagram. The architecture includes:

- **VPC**: 10.0.0.0/16 (Virtual Private Cloud)
- **Public Subnet**: 10.0.1.0/24 - EC2 with Ollama + OpenWebUI
- **Private Subnet**: 10.0.2.0/24 - EMR cluster
- **EMR Subnet**: 10.0.3.0/24 - Data processing
- **Internet Gateway**: Connects VPC to public internet
- **Security Group**: Firewall rules for EC2 (ports 22, 80, 443, 11434, 3000)
- **Load Balancer**: Distributes traffic
- **S3 Bucket**: 25xrvl-s3 - Data and model storage
- **EC2 g4dn.xlarge**: GPU instance for model serving
- **Ollama**: LLM runner
- **OpenWebUI**: Web chat interface

## data flow

1. Raw dataset downloaded from Hugging Face
2. Data uploaded to S3 bucket (25xrvl-s3)
3. EMR cluster runs PySpark preprocessing: filter by language, clean, tokenize
4. Preprocessed data saved to S3
5. Colab loads data from S3 for fine-tuning (QLoRA)
6. Fine-tuned model exported to GGUF, uploaded to S3
7. EC2 instance downloads GGUF from S3
8. Ollama serves model via API
9. OpenWebUI connects to Ollama for browser chat
10. User interacts via web browser