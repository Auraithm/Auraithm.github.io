# Aha: A High-Performance and Efficient Diffusion Language Model

[Ying Zhu](#)<sup>1,2</sup>, [Jiaxin Wan](#)<sup>3,2</sup>, [Tianyi Liang](#)<sup>4,2</sup>, [Xu Guo](#)<sup>1,2</sup>, [Xiaoran Liu](#)<sup>1,2</sup>, [Zengfeng Huang](#)<sup>1,2</sup>, [Ziwei He](#)<sup>2</sup>, [Xipeng Qiu](#)<sup>1,2</sup>

<sup>1</sup>Fudan University, <sup>2</sup>Shanghai Innovation Institute, <sup>3</sup>University of Electronic Science and Technology of China, <sup>4</sup>East China Normal University

[![arXiv](https://img.shields.io/badge/arXiv-2501.XXXXX-b31b1b.svg)](https://arxiv.org/abs/YOUR_PAPER_ID)
[![Paper](https://img.shields.io/badge/Paper-PDF-red.svg)](https://arxiv.org/pdf/YOUR_PAPER_ID.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black.svg?logo=github)](https://github.com/YOUR_REPO_HERE)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow.svg)](https://huggingface.co/YOUR_MODEL_HERE)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)


![Aha Framework Overview](static/images/accuracy.png)

## TL;DR

We introduce **Aha**, a high-performance open-source diffusion large language model (DLLM), alongside an open-source post-training framework specifically designed for efficient and scalable DLLM adaptation. Our framework supports long-context post-training up to 8K tokens, dramatically reducing computational cost while preserving model stability and convergence.

Built upon this framework, Aha achieves state-of-the-art (SOTA) results among models of similar parameter scale, surpassing existing post-training approaches in both efficiency and generalization. This release establishes a practical, fully open foundation for advancing long-context DLLM post-training and adaptation research.

## HighLights

- **🚀 Training — Efficient Post-Training Framework:** An open-source post-training framework specifically designed for DLLMs.
- **⚡ Speed — Parallel Decoding:** Up to 32× speedup in inference time.
- **🧠 Performance — Advanced Science Reasoning Benchmarks:** High scores on MATH and AIME.

## Method

**Aha-8B-Instruct** is developed based on **SDAR-8B-Chat** as the base model, and trained within our open-source **diffusion post-training framework** consisting of two stages: *Supervised Fine-Tuning (SFT)* and *Reinforcement Learning (RL)*.

### Stage 1: Supervised Fine-Tuning (SFT)

We fine-tune the model with a generation length of **2K**, using a high-quality dataset of **2K samples synthesized by Qwen3-Max**. The data are carefully filtered to ensure diversity, correctness, and sequence-length consistency with training requirements.

### Stage 2: Reinforcement Learning (RL)

We adopt the **Trace-RL** algorithm to optimize reasoning robustness and long-context performance. The generation length is extended to **8K**, and we integrate a diffusion-generated step map during optimization to accelerate convergence and stabilize gradient updates.

This two-stage design enables **Aha-8B-Instruct** to achieve efficient long-context adaptation while preserving stability and strong generalization across mathematical reasoning benchmarks.


## Performance

Compared with the base model **SDAR-8B-Chat** and other strong instruction-tuned models, **Aha-8B-Instruct** achieves consistent and substantial improvements across all benchmarks. On *MATH500*, our model reaches **81.60%** accuracy, surpassing the base model by **+9.75%** and outperforming the previous best **Trado-8B-Instruct** (75.59%) by a large margin. On *GSM8K*, **Aha-8B-Instruct** attains **90.65%**, with a **+0.78%** gain over **SDAR-8B-Chat**.

Notably, for the challenging *AIME2024* and *AIME2025* competitions, our model achieves **20.00%** and **19.17%**, improving upon the base model by **+10.83%** and **+9.79%**, respectively. On *OlympiadBench*, **Aha-8B-Instruct** also shows a strong gain of **+8.78%** (44.81% vs. 36.03%), demonstrating superior reasoning depth and problem-solving robustness. Remarkably, **Aha-8B-Instruct** delivers performance comparable to much larger models such as **Qwen2.5-32B-Instruct**.

| Model | MATH500 | GSM8K | AIME2024 | AIME2025 | OlympiadBench |
|-------|---------|-------|----------|----------|---------------|
| Qwen2.5-7B-Instruct | 73.78 | 89.78 | 8.96 | 5.63 | 36.58 |
| Qwen2.5-32B-Instruct | 81.13 | **94.03** | 12.92 | 11.88 | **45.65** |
| SDAR-8B-Chat | 71.85 | 89.87 | 9.17 | 9.38 | 36.03 |
| Trado-8B-Instruct | 75.59 | 91.06 | 11.67 | 15.00 | 40.32 |
| **Aha-8B-Instruct (ours)** | **81.60** | 90.65 | **20.00** | **19.17** | 44.81 |
