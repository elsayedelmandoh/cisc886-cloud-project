# what to submit

## Section 5 - Model Fine-Tuning (6 marks)

### Code

1. **Runnable notebook (.ipynb)** committed to GitHub with:
   - Full training code with inline comments
   - Model loading with quantization
   - LoRA/PEFT configuration
   - Dataset loading from S3
   - Training loop
   - Export to GGUF

### Report Content

2. **Fine-tuning approach table** documenting:
   - Library used (Unsloth)
   - Technique (QLoRA, LoRA, etc.)
   - Hardware (Colab T4, etc.)

3. **Hyperparameter table** including at minimum:
   - Learning rate
   - Batch size
   - Number of epochs
   - LoRA rank (r), alpha, dropout
   - Max sequence length
   - Random seed

4. **Qualitative comparison** with at least 2 example prompts:
   - Base model response
   - Fine-tuned model response
   - Side-by-side table showing improvement

### Optional (encouraged)

- Training loss curve
- Hyperparameter table in report
- Side-by-side comparison screenshots

> What to submit: Runnable notebook (.ipynb) committed to GitHub and a written section in the report documenting your training setup and qualitative comparison
