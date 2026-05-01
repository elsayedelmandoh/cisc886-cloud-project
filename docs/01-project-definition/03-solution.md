# solution overview and approach

## product description

A cloud-based autonomous tech support and coding assistant that provides instant coding help by answering programming questions, debugging code, and explaining concepts.

## main user flow

1. User accesses web interface via browser
2. User types coding question or pastes code
3. System sends query to fine-tuned TinyLlama model via Ollama API
4. Model generates response with coding assistance
5. Response displayed in web interface

## key implementation ideas

1. **Fine-tuning approach**: Use QLoRA with 4-bit quantization on Unsloth for memory efficiency
2. **Base model**: TinyLlama-1.1B-Chat-v1.0 (optimized for Colab T4)
3. **Dataset processing**: PySpark pipeline on AWS EMR for filtering and preprocessing
4. **Deployment**: Export to GGUF format for Ollama serving on EC2
5. **Interface**: OpenWebUI for browser-based chat

