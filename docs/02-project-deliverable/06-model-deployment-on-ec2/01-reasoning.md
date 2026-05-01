# section 6: model deployment on ec2 (3 marks)

## ec2 instance configuration

| Setting | Value |
|---------|-------|
| Instance Name | 25xrvl-ec2 |
| Instance Type | g4dn.xlarge |
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
FROM ./25xrvl-tinyllama-codegpt-q4_k_m.gguf
PARAMETER temperature 0.7
SYSTEM You are a coding assistant.
EOF

# Import model to Ollama
ollama create 25xrvl-codegpt -f Modelfile

# Test
ollama run 25xrvl-codegpt "Hello"
```

## api curl test

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "25xrvl-codegpt",
  "prompt": "Write hello world in Python",
  "stream": false
}'
```

## required screenshots

- [ ] Terminal screenshot showing Ollama serving with model name visible
- [ ] Curl API response screenshot