# Aha: A High-Performance and Efficient Diffusion Language Model

[Ying Zhu](#)<sup>1,2</sup>, [Jiaxin Wan](#)<sup>3,2</sup>, [Tianyi Liang](#)<sup>4,2</sup>, [Xu Guo](#)<sup>1,2</sup>, [Xiaoran Liu](#)<sup>1,2</sup>, [Zengfeng Huang](#)<sup>1,2</sup>, [Ziwei He](#)<sup>2,†</sup>, [Xipeng Qiu](#)<sup>1,2,†</sup>

<sup>1</sup>Fudan University, <sup>2</sup>Shanghai Innovation Institute, <sup>3</sup>University of Electronic Science and Technology of China, <sup>4</sup>East China Normal University

[![arXiv](https://img.shields.io/badge/arXiv-2501.XXXXX-b31b1b.svg)](https://arxiv.org/abs/YOUR_PAPER_ID)
[![Paper](https://img.shields.io/badge/Paper-PDF-red.svg)](https://arxiv.org/pdf/YOUR_PAPER_ID.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black.svg?logo=github)](https://github.com/Auraithm/GTPO-Trainer)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow.svg)](https://huggingface.co/YOUR_MODEL_HERE)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)


![Aha Framework Overview](static/images/accuracy.png)

## TL;DR

We are excited to introduce **GTPO-Trainer**, a comprehensive, open-source training framework for Diffusion Language Models (DLLMs) that encompasses both Supervised Fine-tuning (SFT) and Reinforcement Learning (RL). For SFT, We adopt a high-quality mathematical dataset and utilize a random-masking strategy during SFT to boost reasoning. For RL, we developed **GTPO (Group Trajectory Policy Optimization)**, a novel algorithm inspired by Trace-RL and GRPO, which is specifically tailored for DLLMs and engineered for efficient, multi-node training. Leveraging this framework, we release SDAR-8B-GTPO, an 8B model that achieves state-of-the-art results for its size.

We propose **GTPO (Group Trajectory Policy Optimization)**, a reinforcement learning algorithm specially designed for Diffusion Language Models (DLLMs). It is inspired by Trace-RL's trajectory-level training objective and incorporates the group-based advantage mechanism from GRPO. Importantly, we achieve a perfect and unbiased implementation of RL theory for DLLMs.

Furthermore, we develop a complete training framework, GTPO-DLLM, based on GTPO, which includes a two-stage post-training pipeline: SFT and RL. We integrate the **Lmdeploy** inference framework to enable efficient rollout and step_map feedback, and use **Accelerate** to support multi-node training.

Based on this training framework, we employ the post-training on SDAR-8B-Chat and sucessfully train and release a new difusion language model - **Aha-8B-Instruct**, a high-performance, open-source DLLM that achieves state-of-the-art (SOTA) results among models of comparable scale.

## HighLights

- **🚀 Efficient Training:** Supports **Accelerate** distributed training and **LMDeploy** inference engine for efficient rollout, significantly accelerating the training process.
- **⚡ Speed Optimization:** Integrates **speed reward** mechanism to optimize inference speed at the training level, enabling faster generation without sacrificing quality.
- **🧠 SOTA Performance:** Achieves state-of-the-art results on most mathematical reasoning benchmarks, including MATH, GSM8K, AIME, and OlympiadBench.

## Method

Inspired by the **DLLM-RL** framework, we further develop and release an open-source **diffusion post-training framework** specifically designed for mathematical reasoning. **Aha-8B-Instruct** is developed based on **SDAR-8B-Chat** as the base model, and trained through two stages: *Supervised Fine-Tuning (SFT)* and *Reinforcement Learning (RL)*.

### Stage 1: Supervised Fine-Tuning (SFT)

We prepare a proprietary, high-quality mathematical dataset with a generation length of **8K** tokens. We adopt a random-masking strategy to construct the training data for model fine-tuning.

### Stage 2: Reinforcement Learning (RL)

Inspired by the theoretical foundations of **TraceRL** and **GRPO**, we design an RL framework -- **GTPO**, specifically tailored for DLLMs, training with a generation length of **8K**. Importantly, we achieve a perfect and unbiased implementation of RL theory for DLLMs, ensuring complete consistency between the optimization objective and the actual training process. This algorithm integrates diffusion-specific optimization strategies, including a diffusion-generated step map to accelerate convergence and stabilize gradient updates. The online learning paradigm enables dynamic exploration and continuous improvement during the training process.

This two-stage design enables **Aha-8B-Instruct** to achieve efficient long-context adaptation while preserving stability and strong generalization across mathematical reasoning benchmarks.


## Performance

**Aha-8B-Instruct** achieves state-of-the-art results among DLLMs across mathematical reasoning benchmarks. Highlights include **81.60%** on MATH500 (surpassing the base model by **+9.75%**), **20.00%** on AIME2024 and **19.17%** on AIME2025 (dramatically outperforming all baselines), and **44.81%** on OlympiadBench. Our 8B model achieves performance comparable to or exceeding much larger 32B models on most benchmarks.

| Model | MATH500 | GSM8K | AIME2024 | AIME2025 | OlympiadBench |
|-------|---------|-------|----------|----------|---------------|
| Qwen2.5-7B-Instruct | 73.78 | 89.78 | 8.96 | 5.63 | 36.58 |
| Qwen2.5-32B-Instruct | 81.13 | **94.03** | 12.92 | 11.88 | **45.65** |
| SDAR-8B-Chat | 71.85 | 89.87 | 9.17 | 9.38 | 36.03 |
| Trado-8B-Instruct | 75.59 | 91.06 | 11.67 | 15.00 | 40.32 |
| **Aha-8B-Instruct (ours)** | **81.60** <br/><sub style="color: #28a745;">(+9.75)</sub> | 90.65 <br/><sub style="color: #28a745;">(+0.78)</sub> | **20.00** <br/><sub style="color: #28a745;">(+10.83)</sub> | **19.17** <br/><sub style="color: #28a745;">(+9.79)</sub> | 44.81 <br/><sub style="color: #28a745;">(+8.78)</sub> |
