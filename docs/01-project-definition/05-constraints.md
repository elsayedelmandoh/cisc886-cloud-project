# project constraints and assumptions

## compute constraints

- Fine-tuning on Google Colab (free T4, 16GB VRAM)
- Requires QLoRA with 4-bit quantization for memory efficiency
- Max sequence length: 2048 tokens for TinyLlama

## cost constraints

- AWS credits available but limited
- Must terminate EMR cluster after use
- Use spot instances where possible

## data quality constraints

- Code snippets only (no conversational pairs)
- Need to format for instruction tuning
- Quality varies across repositories

## deployment constraints

- Must prefix all AWS resources with 25xrvl
- EC2 g4dn.xlarge for GPU inference
- Ollama for model serving

## timeline constraints

- 5 days total for 3 team members
- Sequential phases: preprocessing → fine-tuning → deployment → testing
