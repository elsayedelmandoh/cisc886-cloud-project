# research notes


## models 

1) unsloth/Qwen2.5-Coder-7B-Instruct

> why?

primarily made for code (not general)
instruct version > already understands commands
we can fine-tune it further (for a specific style or custom tasks)

with the unsloth version:

we can fine-tune faster and cheaper (qloRA / peft)
very suitable if our resources are limited

this is a "production-level starter" choice

> choose instruct cuz we save time and higher performance from the start


2) TinyLlama/TinyLlama-1.1B-Chat-v1.0

> why?

not suitable as a strong coding assistant
very small (1.1b)
not specialized in code
even after fine-tuning > limited performance

good only for:

experimenting
learning
lightweight prototype

> choose base cuz we need more data + harder work

>> final choose: tinyllama + fine tuning


## datasets

1) bigcode/the-stack

This dataset contains terabytes of permissively licensed source code across hundreds of programming languages. It provides an excellent foundation for an autonomous coding assistant and gives you plenty of raw data to filter, clean, and format using Apache Spark on your AWS EMR cluster.

2) Stack Exchange Data Dump 

This dump contains the entire history of Q&A from tech-heavy sites like Stack Overflow and Server Fault. Processing the raw XML dumps into clean instruction response pairs is a perfect, rigorous workload for your distributed PySpark pipeline before fine-tuning.