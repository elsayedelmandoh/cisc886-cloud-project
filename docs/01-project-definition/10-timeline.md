# project timeline and milestones

## 5-day timeline for 3 members

### Day 1: Infrastructure & Data Acquisition

| Task | Owner | Deliverable |
|------|-------|------------|
| Create VPC 25xrvl-VPC | Member 1 | Terraform or console screenshot |
| Create S3 bucket 25xrvl-s3-project | Member 1 | S3 console screenshot |
| Download bigcode/the-stack-smol | Member 2 | Local dataset |
| Filter by language (Python, JS, Java, Go) | Member 2 | 300K filtered samples |

### Day 2: Data Preprocessing with EMR

| Task | Owner | Deliverable |
|------|-------|------------|
| Upload data to S3 | Member 2 | S3 files |
| Launch EMR cluster | Member 1 | EMR console screenshot |
| Run PySpark preprocessing | Member 2 | Preprocessed output in S3 |
| Terminate EMR cluster | Member 1 | Teardown screenshot |

### Day 3: Model Fine-tuning

| Task | Owner | Deliverable |
|------|-------|-------------|
| Load dataset in Colab | Member 3 | Connected to S3 |
| Fine-tune with QLoRA | Member 3 | LoRA adapter |
| Compare base vs fine-tuned | Member 3 | 2+ example prompts |

### Day 4: Export & Deployment

| Task | Owner | Deliverable |
|------|-------|-------------|
| Export to GGUF | Member 3 | GGUF file |
| Upload to S3 | Member 3 | S3 GGUF file |
| Launch EC2 g4dn.xlarge | Member 1 | Instance running |
| Install Ollama + load model | Member 1 | Ollama serving |
| Setup OpenWebUI | Member 2 | Web interface |

### Day 5: Testing & Documentation

| Task | Owner | Deliverable |
|------|-------|-------------|
| API curl test | Member 1 | Response screenshot |
| Web interface test | Member 2 | Browser screenshot |
| Collect all screenshots | All | Report sections |
| Finalize report | All | Complete PDF |
| Teardown AWS resources | Member 1 | Final screenshots |

## milestones

- [ ] VPC and S3 created with 25xrvl prefix
- [ ] Dataset filtered and in S3
- [ ] EMR cluster terminated (screenshot required)
- [ ] Fine-tuned model on Colab
- [ ] GGUF exported
- [ ] EC2 deployment with Ollama
- [ ] OpenWebUI accessible
- [ ] All report sections complete
