# project goal and success criteria

## measurable outcome

Build and deploy a cloud-based autonomous tech support and coding assistant by fine-tuning TinyLlama-1.1B on code-related data from bigcode/the-stack-smol dataset, deploy to AWS EC2, and provide a web-based chat interface.

## success criteria

| Metric | Target |
|--------|--------|
| Base model | TinyLlama-1.1B-Chat-v1.0 |
| Dataset size | 300K samples (Python, JavaScript, Java, Go) |
| Fine-tuning method | QLoRA (4-bit quantization) |
| Deployable format | GGUF for Ollama |
| Web interface | OpenWebUI accessible via browser |
| VPC with proper networking | 25xrvl-VPC with public/private subnets |
| EMR preprocessing | PySpark pipeline on AWS EMR |
| EC2 deployment | g4dn.xlarge instance with Ollama |

## how you will know it worked

1. Fine-tuned model responds to coding queries with domain-appropriate answers
2. Model serves via Ollama on EC2 and responds to API calls
3. Web interface loads in browser and shows model responses
4. All AWS resources created with 25xrvl prefix and properly torn down

