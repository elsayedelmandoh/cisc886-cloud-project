# project proposal summary and scope

## section 1: system architecture (2 marks)


## section 2: vpc and networking (4 marks)


## section 3: model & dataset selection (3 marks)

### model selection

| Attribute | Value |
|-----------|-------|
| Model name | TinyLlama-1.1B-Chat-v1.0 |
| Parameters | 1.1 billion |
| Source | Hugging Face: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 |
| License | Apache 2.0 |

#### why tinyllama is appropriate

1. **Size**: 1.1B parameters fits within 16GB VRAM (Colab T4) with 4-bit quantization
2. **Hardware requirements**: Feasible for fine-tuning on free Colab + deployment on g4dn.xlarge
3. **Domain fit**: Pre-trained on 30% code data (Starcoderdata), suitable for coding assistant task
4. **Training ratio**: 7:3 natural language to code ratio ensures both conversation and coding capability
5. **Efficiency**: Unsloth provides 2-4x faster training, 70%+ memory reduction
6. **Chat capability**: TinyLlama-1.1B-Chat-v1.0 has instruction tuning for conversational use

### dataset selection

| Attribute | Value |
|-----------|-------|
| Dataset name | bigcode/the-stack-smol |
| Source | Hugging Face: https://huggingface.co/datasets/bigcode/the-stack-smol |
| License | Apache 2.0 |
| Total samples | ~300K code samples |

#### languages selected

- Python
- JavaScript
- Go

#### split strategy

- Training: 80% (240K samples)
- Validation: 10% (30K samples)
- Test: 10% (30K samples)

#### data leakage avoidance

1. No overlapping commits across splits (by hexsha)
2. Random shuffle before split with fixed seed
3. No data from same repository in train and test

#### sample data (verbatim)

```
language: python
content: def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

#### summary statistics

| Language | Count | Percentage |
|---------|-------|------------|
| Python | ~150K | 50% |
| JavaScript | ~75K | 25% |
| Java | ~50K | 17% |
| Go | ~25K | 8% |

Average token length per sample: ~256 tokens

