# section 6: model deployment on ec2 (3 marks)

## ec2 instance configuration

| Setting | Value |
|---------|-------|
| Instance Name | 25xrvl-ec2 |
| Instance Type | t3.2xlarge |
| AMI | Deep Learning AMI (Ubuntu 20.04) |
| Region | us-east-1 |
| Storage | 100 GB gp3 |

## installation commands

```bash
# SSH into EC2
ssh -i "25xrvl-key.pem" ubuntu@ec2-*.us-east-1.compute.amazonaws.com

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download model from S3
aws s3 cp s3://25xrvl-s3/models/25xrvl-tinyllama-codegpt-q4_k_m.gguf .

# Create Modelfile
cat > Modelfile << EOF
FROM ./my_model/model_final.gguf 
PARAMETER temperature 0.7
SYSTEM You are a coding assistant.
EOF

# Clone conversion tool
git clone https://github.com/ggerganov/llama.cpp

# Install dependencies
pip install gguf sentencepiece numpy transformers torch --break-system-packages

# Run conversion
python3 llama.cpp/convert_hf_to_gguf.py ~/my_model --outfile ~/my_model/model_final.gguf --outtype q8_0


# Import model to Ollama
ollama create 25xrvl-codegpt -f Modelfile

# Test
ollama run codegpt-25xrvl "Write a hello world in Python"


# api curl test

curl http://localhost:11434/api/tags
```

## required screenshots

- [ ] Terminal screenshot showing Ollama serving with model name visible
- [ ] Curl API response screenshot