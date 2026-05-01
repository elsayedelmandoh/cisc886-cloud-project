# stack overview and tooling choices

## expertise

ml, dl, nlp, genai, agentic ai

## core stack

- language: python 3.12
- environment: conda
- entrypoint: app.py
- reusable code: src/
- tests: tests/
- notebooks: notebooks/
- docs: docs/
- data layout: data/raw, data/processed, data/samples, data/models, data/predictions, data/vectorizers, data/remote_cache
- project manager: gemini 3.1 pro
- ide: vscode (wsl2)
- architect: claude 4.6 opus
- implementation: glm5, kimi k2.5, qwen 3.6 pro
- code review: claude 4.6 opus
- deployment: hugging face, docker

## ml/dl tooling

- pytorch
- transformers
- peft (lora, qlora)
- unsloth (fine-tuning with 4-bit quantization)
- bitsandbytes (4-bit quantization)
- accelerate (distributed training)

## cloud infrastructure

- aws cli
- boto3 (s3, emr, ec2)
- pyarrow / pandas (data handling)
- pyspark (emr preprocessing)

## model serving

- ollama (local llm runner)
- llama.cpp / gguf (model conversion)
- open-webui (web interface)

## common libraries

- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn
- scipy
- nltk
- datasets (hugging face)

## project rules

- keep dependencies minimal until a feature needs them
- add a library only when it supports a concrete use case
- keep notebooks for exploration and move stable logic into src/
- keep tests deterministic and repeatable

