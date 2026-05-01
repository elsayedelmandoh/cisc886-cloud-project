# end-to-end workflow and handoff points

## project phases

| Phase | Component | Assignee | Deliverable |
|-------|-----------|----------|-------------|
| 1 | AWS Infrastructure | Team member 1 | VPC, S3 bucket, security groups |
| 2 | Data Preprocessing | Team member 2 | EMR PySpark pipeline → filtered data in S3 |
| 3 | Model Fine-tuning | Team member 3 | QLoRA fine-tuned model on Colab |
| 4 | Model Export | Team member 3 | GGUF model for Ollama |
| 5 | EC2 Deployment | Team member 1 | Ollama serving fine-tuned model |
| 6 | Web Interface | Team member 2 | OpenWebUI running in browser |
| 7 | Testing & Report | All members | Screenshots, documentation |

## handoff points

1. **S3 data ready** → Colab fine-tuning can begin
2. **Fine-tuning complete** → Export to GGUF
3. **GGUF in S3** → EC2 deployment
4. **EC2 running** → Web interface setup

