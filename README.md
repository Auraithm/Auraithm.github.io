# Aha: A High-Performance and Efficient Diffusion Language Model

[Ying Zhu](#)<sup>1,2</sup>, [Jiaxin Wan](#)<sup>3,2</sup>, [Tianyi Liang](#)<sup>4,2</sup>, [Xu Guo](#)<sup>1,2</sup>, [Xiaoran Liu](#)<sup>1,2</sup>, [Zengfeng Huang](#)<sup>1,2</sup>, [Ziwei He](#)<sup>2</sup>, [Xipeng Qiu](#)<sup>1,2</sup>

---

![Aha Framework Overview](static/images/accuracy.png)

## TL;DR

We introduce **Aha**, a high-performance open-source diffusion large language model (DLLM), alongside an open-source post-training framework specifically designed for efficient and scalable DLLM adaptation. Our framework supports long-context post-training up to 8K tokens, dramatically reducing computational cost while preserving model stability and convergence.

Built upon this framework, Aha achieves state-of-the-art (SOTA) results across multiple mathematical and reasoning benchmarks, surpassing existing post-training approaches in both efficiency and generalization. This release establishes a practical, fully open foundation for advancing long-context DLLM post-training and adaptation research.

## HighLights

- **🚀 Training — Efficient Post-Training Framework:** An open-source post-training framework specifically designed for DLLMs.
- **⚡ Speed — Parallel Decoding:** Up to 32× speedup in inference time.
- **🧠 Performance — Advanced Science Reasoning Benchmarks:** High scores on MATH and AIME.

## Method

**Aha-Math-8B-Instruct** is developed based on **SDAR-8B-Chat** as the base model, and trained within our open-source **diffusion post-training framework** consisting of two stages: *Supervised Fine-Tuning (SFT)* and *Reinforcement Learning (RL)*.

### Stage 1: Supervised Fine-Tuning (SFT)

We fine-tune the model with a generation length of **2K**, using a high-quality dataset of **2K samples synthesized by Qwen3-Max**. The data are carefully filtered to ensure diversity, correctness, and sequence-length consistency with training requirements.

### Stage 2: Reinforcement Learning (RL)

We adopt the **Trace-RL** algorithm to optimize reasoning robustness and long-context performance. The generation length is extended to **8K**, and we integrate a **diffusion-generated step map** during optimization to accelerate convergence and stabilize gradient updates.

This two-stage design enables **Aha-Math-8B-Instruct** to achieve efficient long-context adaptation while preserving stability and strong generalization across mathematical reasoning benchmarks.


## Performance

Compared with existing instruction-tuned mathematical models, **Aha-Math-8B-Instruct** demonstrates remarkable and consistent performance gains across all evaluated benchmarks. On *MATH500*, our model achieves **82.37**, outperforming the previous best (*Trado-8B-Instruct*) by **+6.78** points. On *GSM8K*, it improves accuracy by **+2.94** (94.00 vs. 91.06). For the more challenging *AIME2024* and *AIME2025* competitions, **Aha-Math-8B-Instruct** yields gains of **+5.33** and **+1.00** points, respectively, indicating stronger generalization to advanced and unseen mathematical problems.

These results demonstrate that our post-training framework substantially enhances mathematical reasoning and generalization performance.

| Model | MATH500 | GSM8K | AIME2024 | AIME2025 |
|-------|---------|-------|----------|----------|
| Qwen2.5-Math-7B-Instruct | 75.10 | 89.90 | 16.67 | 0.00 |
| SDAR-8B-Chat | 71.85 | 89.87 | 9.17 | 9.38 |
| Trado-8B-Instruct | 75.59 | 91.06 | 11.67 | 15.00 |
| **Aha-Math-8B-Instruct (ours)** | **82.37** | **94.00** | **17.00** | **16.00** |
