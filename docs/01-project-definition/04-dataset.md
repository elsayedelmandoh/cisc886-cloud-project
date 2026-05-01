# dataset scope, source, and constraints

## source

- **Dataset**: bigcode/the-stack-smol
- **Hugging Face**: https://huggingface.co/datasets/bigcode/the-stack-smol
- **License**: Apache 2.0

## size

- Total samples: ~300K code samples
- Languages included: Python, JavaScript, Java, Go

## schema

| Field | Type | Description |
|-------|------|-------------|
| hexsha | string | Git commit SHA |
| repo | string | Repository name |
| path | string | File path |
| language | string | Programming language |
| content | string | Source code content |
| size | int | File size in bytes |
| license | string | License identifier |

## filtering strategy

1. Filter by language: Python, JavaScript, Java, Go
2. Remove samples with ambiguous or unknown licenses
3. Train/validation/test split: 80/10/10

## refresh strategy

Static dataset - no refresh needed for this project.

## privacy and licensing limits

- Apache 2.0 license allows commercial use and modification
- No PII in code datasets
- Attribution required per license terms
