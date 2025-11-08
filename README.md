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

We propose **Aha-DLLM**, a block-attention based diffusion large language model (DLLM) post-training framework that supports two-stage training: Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). 

Based on this framework, we perform two-stage post-training on SDAR-8B-Chat and release **Aha-8B-Instruct**, a high-performance, open-source DLLM that achieves state-of-the-art (SOTA) results among models of comparable scale.

## HighLights

- **🚀 Efficient Training:** Supports **Accelerate** distributed training and **LMDeploy** inference engine for efficient rollout, significantly accelerating the training process.
- **⚡ Speed Optimization:** Integrates **speed reward** mechanism to optimize inference speed at the training level, enabling faster generation without sacrificing quality.
- **🧠 SOTA Performance:** Achieves state-of-the-art results on most mathematical reasoning benchmarks, including MATH, GSM8K, AIME, and OlympiadBench.

## Method

Inspired by the **DLLM-RL** framework, we further develop and release an open-source **diffusion post-training framework** specifically designed for mathematical reasoning. **Aha-8B-Instruct** is developed based on **SDAR-8B-Chat** as the base model, and trained through two stages: *Supervised Fine-Tuning (SFT)* and *Reinforcement Learning (RL)*.

### Stage 1: Supervised Fine-Tuning (SFT)

We fine-tune the model using a proprietary high-quality mathematical dataset with a generation length of **8K**. Following the data curation strategy from **DAPO**, we apply rigorous filtering to ensure data quality, diversity, and correctness, which lays a solid foundation for subsequent RL training.

### Stage 2: Reinforcement Learning (RL)

We design an **online RL algorithm** specifically tailored for DLLMs, training with a generation length of **8K**. This algorithm integrates diffusion-specific optimization strategies, including a diffusion-generated step map to accelerate convergence and stabilize gradient updates. The online learning paradigm enables dynamic exploration and continuous improvement during the training process.

This two-stage design enables **Aha-8B-Instruct** to achieve efficient long-context adaptation while preserving stability and strong generalization across mathematical reasoning benchmarks.


## Performance

We compare **Aha-8B-Instruct** with both autoregressive (AR) models (**Qwen2.5-7B-Instruct** and **Qwen2.5-32B-Instruct**) and diffusion language models (DLLMs, including **SDAR-8B-Chat** and **Trado-8B-Instruct**). **Aha-8B-Instruct** demonstrates exceptional performance across mathematical reasoning benchmarks, achieving state-of-the-art results among DLLMs and even surpassing much larger AR models. 

On **MATH500**, our model reaches **81.60%** accuracy, not only surpassing the base model **SDAR-8B-Chat** (71.85%) by **+9.75%** and outperforming **Trado-8B-Instruct** (75.59%) by **+6.01%**, but also exceeding the much larger **Qwen2.5-32B-Instruct** (81.13%) to achieve the best performance across all compared models.

On the highly challenging competition benchmarks, **Aha-8B-Instruct** shows remarkable capabilities. For **AIME2024**, our model achieves **20.00%**, dramatically outperforming all baselines including **Qwen2.5-32B-Instruct** (12.92%) by **+7.08%**, **Trado-8B-Instruct** (11.67%) by **+8.33%**, and the base model (9.17%) by **+10.83%**. Similarly, on **AIME2025**, **Aha-8B-Instruct** attains **19.17%**, substantially surpassing **Trado-8B-Instruct** (15.00%) by **+4.17%**, **Qwen2.5-32B-Instruct** (11.88%) by **+7.29%**, and the base model (9.38%) by **+9.79%**.

On **OlympiadBench**, **Aha-8B-Instruct** achieves **44.81%**, showing a significant improvement of **+8.78%** over **SDAR-8B-Chat** (36.03%) and **+4.49%** over **Trado-8B-Instruct** (40.32%), approaching the performance of **Qwen2.5-32B-Instruct** (45.65%). On **GSM8K**, our model attains **90.65%**, maintaining competitive performance with the base model (89.87%).

These results demonstrate that **Aha-8B-Instruct**, as an 8B-scale model, achieves performance comparable to or exceeding much larger 32B models on most benchmarks, showcasing the effectiveness of our diffusion post-training framework.

| Model | MATH500 | GSM8K | AIME2024 | AIME2025 | OlympiadBench |
|-------|---------|-------|----------|----------|---------------|
| Qwen2.5-7B-Instruct | 73.78 | 89.78 | 8.96 | 5.63 | 36.58 |
| Qwen2.5-32B-Instruct | 81.13 | **94.03** | 12.92 | 11.88 | **45.65** |
| SDAR-8B-Chat | 71.85 | 89.87 | 9.17 | 9.38 | 36.03 |
| Trado-8B-Instruct | 75.59 | 91.06 | 11.67 | 15.00 | 40.32 |
| **Aha-8B-Instruct (ours)** | **81.60** <br/><sub style="color: #28a745;">(+9.75)</sub> | 90.65 <br/><sub style="color: #28a745;">(+0.78)</sub> | **20.00** <br/><sub style="color: #28a745;">(+10.83)</sub> | **19.17** <br/><sub style="color: #28a745;">(+9.79)</sub> | 44.81 <br/><sub style="color: #28a745;">(+8.78)</sub> |
