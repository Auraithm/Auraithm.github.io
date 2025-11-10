# Aha: A High-Performance and Efficient Diffusion Language Model

[Ying Zhu](#)<sup>1,2</sup>, [Jiaxin Wan](#)<sup>3,2</sup>, [Tianyi Liang](#)<sup>4,2</sup>, [Xu Guo](#)<sup>1,2</sup>, [Xiaoran Liu](#)<sup>1,2</sup>, [Zengfeng Huang](#)<sup>1,2</sup>, [Ziwei He](#)<sup>2,†</sup>, [Xipeng Qiu](#)<sup>1,2,†</sup>

<sup>1</sup>Fudan University, <sup>2</sup>Shanghai Innovation Institute, <sup>3</sup>University of Electronic Science and Technology of China, <sup>4</sup>East China Normal University

<sup>†</sup>Corresponding authors

[![arXiv](https://img.shields.io/badge/arXiv-2501.XXXXX-b31b1b.svg)](https://arxiv.org/abs/YOUR_PAPER_ID)
[![Paper](https://img.shields.io/badge/Paper-PDF-red.svg)](https://arxiv.org/pdf/YOUR_PAPER_ID.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Code-black.svg?logo=github)](https://github.com/YOUR_REPO_HERE)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow.svg)](https://huggingface.co/YOUR_MODEL_HERE)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)


![Aha Framework Overview](static/images/accuracy.png)

## TL;DR

We are excited to introduce **GTPO-Trainer**, a comprehensive, open-source training framework for Diffusion Language Models (DLLMs) that encompasses both Supervised Fine-tuning (SFT) and Reinforcement Learning (RL). For SFT, We adopt a high-quality mathematical dataset and utilize a random-masking strategy during SFT to boost reasoning. For RL, we developed **GTPO (Group Trajectory Policy Optimization)**, a novel algorithm inspired by Trace-RL and GRPO, which is specifically tailored for DLLMs and engineered for efficient, multi-node training. Leveraging this framework, we release Aha-8B-Instruct, an 8B model that establishes a new state-of-the-art (SOTA) of its scale.


## HighLights

- **🎯 Novel RL Algorithm:** Proposes **GTPO (Group Trajectory Policy Optimization)**, an RL algorithm inspired by TraceRL and GRPO, specifically tailored for DLLMs. It achieves unbiased implementation with complete consistency between optimization objectives and training process, and integrates dynamic sampling from DAPO during rollout to filter out low-quality data.
- **🚀 Efficient Training & Inference:** Supports **Accelerate** distributed training and **LMDeploy** inference engine for efficient rollout, while integrating **speed reward** mechanism to optimize inference speed at the training level, enabling both faster training and generation without sacrificing quality.
- **🧠 SOTA Performance:** At the 8B scale, our model achieves state-of-the-art results among both autoregressive (AR) models and diffusion language models (DLLMs) across multiple mathematical reasoning benchmarks. Specifically, it reaches **81.60%** on MATH500, **20.00%** on AIME2024, and **19.17%** on AIME2025, surpassing all 8B baselines and even outperforming the 32B Qwen2.5-32B-Instruct model on AIME benchmarks.

## Method

Inspired by the **DLLM-RL** framework, we further develop and release an open-source **diffusion post-training framework** specifically designed for mathematical reasoning. **Aha-8B-Instruct** is developed based on **SDAR-8B-Chat** as the base model, and trained through two stages: *Supervised Fine-Tuning (SFT)* and *Reinforcement Learning (RL)*.

### Stage 1: Supervised Fine-Tuning (SFT)

We prepare a proprietary, high-quality mathematical dataset with a generation length of **8K** tokens. We adopt a random-masking strategy to construct the training data for model fine-tuning.

### Stage 2: Reinforcement Learning (RL)

Inspired by the theoretical foundations of **TraceRL** and **GRPO**, we design an RL framework -- **GTPO**, specifically tailored for DLLMs, training with a generation length of **8K**. We achieve an unbiased implementation of RL theory for DLLMs, ensuring complete consistency between the optimization objective and the actual training process. Additionally, during the rollout phase, we adopt dynamic sampling from DAPO to filter out data with zero advantage standard deviation.

Through this two-stage training pipeline, we successfully train **Aha-8B-Instruct**, a high-performance diffusion language model for mathematical reasoning.


## Performance

**Aha-8B-Instruct** achieves state-of-the-art results among DLLMs across mathematical reasoning benchmarks. Highlights include **81.60%** on MATH500 (surpassing the base model by **+9.75%**), **20.00%** on AIME2024 and **19.17%** on AIME2025 (dramatically outperforming all baselines), and **44.81%** on OlympiadBench. Our 8B model achieves performance comparable to or exceeding much larger 32B models on most benchmarks.

| Model | MATH500 | GSM8K | AIME2024 | AIME2025 | OlympiadBench |
|-------|---------|-------|----------|----------|---------------|
| Qwen2.5-7B-Instruct | 73.78 | 89.78 | 8.96 | 5.63 | 36.58 |
| Qwen2.5-32B-Instruct | 81.13 | **94.03** | 12.92 | 11.88 | **45.65** |
| SDAR-8B-Chat | 71.85 | 89.87 | 9.17 | 9.38 | 36.03 |
| Trado-8B-Instruct | 75.59 | 91.06 | 11.67 | 15.00 | 40.32 |
| **Aha-8B-Instruct (ours)** | **81.60** <br/><sub style="color: #28a745;">(+9.75)</sub> | 90.65 <br/><sub style="color: #28a745;">(+0.78)</sub> | **20.00** <br/><sub style="color: #28a745;">(+10.83)</sub> | **19.17** <br/><sub style="color: #28a745;">(+9.79)</sub> | 44.81 <br/><sub style="color: #28a745;">(+8.78)</sub> |


## Citation

If you find our work helpful, please consider citing:

```bibtex
@article{zhu2025aha,
  title={Aha: A High-Performance and Efficient Diffusion Language Model},
  author={Ying Zhu and Jiaxin Wan and Tianyi Liang and Xu Guo and Xiaoran Liu and Zengfeng Huang and Ziwei He and Xipeng Qiu},
  journal={arXiv preprint arXiv:2501.XXXXX},
  year={2025}
}
```
