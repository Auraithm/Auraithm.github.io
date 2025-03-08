---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
 
{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

# About Me
I am currently an junior undergraduate student at the School of Artificial Intelligence, Nanjing University of Information Science and Technology, where I am fortunate to be advised by [Peilan Xu](https://scholar.google.ca/citations?hl=zh-CN&user=MYTn5zYAAAAJ "许沛澜"). 

My current research focuses on evolutionary computation, LLM reasoning, multi-agent frameworks, and various LLM application research. Several papers have been submitted to the top journals and conferences in the field of artificial intelligence (such as ACM Transactions, IJCAI, ACL ...), and my representative work "Density-Assisted Evolutionary Dynamic Multimodal Optimization" has been accepted by ACM TELO.

Currently, I am undertaking an internship at [Shanghai AI Lab](https://www.shlab.org.cn/ "上海人工智能实验室") under the mentorship of [Rui Su](https://scholar.google.ca/citations?hl=zh-CN&authuser=2&user=tLLmRBwAAAAJ "苏锐"). Concurrently, I am working as a research assistant at The University of Tokyo, and collaborate closely with [Xinjie Zhao]([https://openreview.net/profile?id=~Zhao_Xinjie1](https://scholar.google.com/citations?hl=zh-CN&user=_l5fPvEAAAAJ) "赵新杰"). .

I am honoured to be recognized as a **Kaggle Expert** for winning two silver medals in LLM competitions. Additionally, I won the championship in the [IEEE CEC Competition on Seeking Multiple Optima in Dynamic Environments](http://mi.hitsz.edu.cn/activities/smode_cec2023/index.html) for two consecutive years (2023,2024), and was awarded a national first prize in the Lanqiao Cup.

I am actively seeking opportunities for academic collaboration and would be delighted to discuss potential partnerships. Please feel free to contact me at <auraithm@gmail.com> (personal email) or <evonexusx@gmail.com>.

---

# 🔥 News
- *2025.03*: &nbsp;🎉🎉 Paper "Density-Assisted Evolutionary Dynamic Multimodal Optimization" is accepted by **ACM Transactions on Evolutionary Learning and Optimization**.
- *2025.03*: &nbsp;🎉🎉 Won a silver medal at Kaggle competitions "LLMs - You Can't Please Them All".

---

# 🎖 Honors and Awards
- *2025.03* Won a silver medal at the Kaggle competition **"LLMs - You Can't Please Them All"**.
- *2024.07* Won the championship in the **IEEE CEC 2024 Competition on Seeking Multiple Optima in Dynamic Environments**.
- *2024.06* Won the national first prize in the Lanqiao Cup.
- *2024.04* Won a silver medal at the Kaggle competition **"LLM Prompt Recovery"**.
- *2023.07* Won the championship in the **IEEE CEC 2023 Competition on Seeking Multiple Optima in Dynamic Environments**.

---

# 📝 Publications 
- **Density-Assisted Evolutionary Dynamic Multimodal Optimization**, **YingZhu**, Peilan Xu, Jiahao Huang, Xin Lin, Wenjian Luo, **ACM TELO**.
- **[GRATR: Zero-Shot Evidence Graph Retrieval-Augmented Trustworthiness Reasoning](https://arxiv.org/abs/2408.12333)**, **Ying Zhu\***, Shengchang Li\*, Ziqian Kong, Qiang Yang, Peilan Xu, **IJCAI 2025 (Under the second reviewing phase)**.
- **[Narrative-Driven Travel Planning: Geocultural-Grounded Script Generation with Evolutionary Itinerary Optimization](https://arxiv.org/abs/2502.14456)**, Ran Ding\*, Ziyu Zhang\*, **Ying Zhu\***, Ziqian Kong, Peilan Xu, **ACL 2025 (Under Review)**.
- **ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA**, Zhao Xinjie, Fan Gao, Rui Yang, Yingjian Chen, Yuyang Wang, **Ying Zhu**, Jiacheng Tang, Irene Li , **ACL 2025 (Under Review)**.
- **Adaptive Interruption and Trust-Weighted Voting for Secure Multi-Agent Collaboration in Complex Question Answering**, **Ying Zhu\***, Zhao Xinjie, Irene Li, **arXiv**.

---

# 💬 Research Overview

## **Density-Assisted Evolutionary Dynamic Multimodal Optimization**

**Authors:** **YingZhu**, Peilan Xu, Jiahao Huang, Xin Lin, Wenjian Luo

**Journal: ACM Transactions on Evolutionary Learning and Optimization** (Accept)

**Code: <https://github.com/EvoNexusX/2023ZhuDAEA>**


<div style="text-align: center; margin: 0 auto; max-width: 50%;">
    <div class="badge">ACM TELO</div>
    <img src='images/Density_00.png' alt="sym" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>
 
### Abstract
Dynamic multimodal optimization problems (DMMOPs) demand algorithms capable of swiftly locating and tracking multiple optimal solutions over time. The primary challenge lies in controlling the population diversity to facilitate effective exploration, all within the limitation of computational resources between consecutive environmental changes. In this paper, we study the utilization of density information derived from both current and historical populations to enhance exploration. First, for each active sub-population, we construct a density landscape based on the distribution of concurrently active sub-populations, and establish dominance relationships between candidate solutions in the sub-population based on density and fitness values, directing this sub-population towards exploring low-density promising areas. Then, for each converged sub-population, we construct a density landscape based on the distribution of sub-populations that have historically become extinct, guiding the restart of this sub-population in low-density unexploited areas. Finally, we develop a comprehensive framework of density-assisted evolutionary algorithm (DAEA), which encompasses density-assisted search and restart, also combined with initialization. Moreover, we employ prediction and memory strategies to enhance the performance of DAEA in dynamic environments. Notably, the algorithm relies on an external monitor to detect environmental changes and trigger the dynamic response strategy. DAEA is tested on the CEC'2022 dynamic multimodal optimization benchmark suite, and is compared against several state-of-the-art dynamic multimodal optimization algorithms. The experimental results demonstrate the competitiveness of DAEA in handling DMMOPs.

---

## **[GRATR: Zero-Shot Evidence Graph Retrieval-Augmented Trustworthiness Reasoning](https://arxiv.org/abs/2408.12333)**

**Authors:** **Ying Zhu\***, Shengchang Li\*, Ziqian Kong, Qiang Yang, Peilan Xu.

**Conference: IJCAI 2025** (Under the second reviewing phase)

**Code: <https://github.com/EvoNexusX/2025ZhuGRATR>**


<div style="text-align: center; margin: 0 auto; max-width: 100%;">
    <div class="badge">IJCAI 2025</div>
    <img src='images/fig2_00.png' alt="sym" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>
 
### Abstract

Trustworthiness reasoning aims to enable agents in multiplayer games with incomplete information to identify potential allies and adversaries, thereby enhancing decision-making. In this paper, we introduce the graph retrieval-augmented trustworthiness reasoning (GRATR) framework, which retrieves observable evidence from the game environment to inform decision-making by large language models (LLMs) without requiring additional training, making it a zero-shot approach. Within the GRATR framework, agents first observe the actions of other players and evaluate the resulting shifts in inter-player trust, constructing a corresponding trustworthiness graph. During decision-making, the agent performs multi-hop retrieval to evaluate trustworthiness toward a specific target, where evidence chains are retrieved from multiple trusted sources to form a comprehensive assessment. Experiments in the multiplayer game \emph{Werewolf} demonstrate that GRATR outperforms the alternatives, improving reasoning accuracy by 50.5\% and reducing hallucination by 30.6\% compared to the baseline method. Additionally, when tested on a dataset of Twitter tweets during the U.S. election period, GRATR surpasses the baseline method by 10.4\% in accuracy, highlighting its potential in real-world applications such as intent analysis.
 
---

## **[Narrative-Driven Travel Planning: Geocultural-Grounded Script Generation with Evolutionary Itinerary Optimization](https://arxiv.org/abs/2502.14456)**

**Authors:** Ran Ding\*, Ziyu Zhang\*, **Ying Zhu\***, Ziqian Kong, Peilan Xu.

**Conference: ACL 2025** (Under Review)

**Code: <https://github.com/EvoNexusX/2025DingNarrativeGuide>**


<div style="text-align: center; margin: 0 auto; max-width: 100%;">
    <div class="badge">ACL 2025</div>
    <img src='images/3.png' alt="sym" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>
 
### Abstract

To enhance tourists' experiences and immersion, this paper proposes a narrative-driven travel planning framework called NarrativeGuide, which generates a geoculturally-grounded narrative script for travelers, offering a novel, role-playing experience for their journey. In the initial stage, NarrativeGuide constructs a knowledge graph for attractions within a city, then configures the worldview, character setting, and exposition based on the knowledge graph. Using this foundation, the knowledge graph is combined to generate an independent scene unit for each attraction. During the itinerary planning stage, NarrativeGuide models narrative-driven travel planning as an optimization problem, utilizing a genetic algorithm (GA) to refine the itinerary. Before evaluating the candidate itinerary, transition scripts are generated for each pair of adjacent attractions, which, along with the scene units, form a complete script. The weighted sum of script coherence, travel time, and attraction scores is then used as the fitness value to update the candidate solution set. Experimental results across four cities, i.e., Nanjing and Yangzhou in China, Paris in France, and Berlin in Germany, demonstrate significant improvements in narrative coherence and cultural fit, alongside a notable reduction in travel time and an increase in the quality of visited attractions. Our study highlights that incorporating external evolutionary optimization effectively addresses the limitations of large language models in travel planning.

---

## **ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA**

**Authors:** Zhao Xinjie, Fan Gao, Rui Yang, Yingjian Chen, Yuyang Wang, **Ying Zhu**, Jiacheng Tang, Irene Li.

**Conference: ACL 2025** (Under Review)

<div style="text-align: center; margin: 0 auto; max-width: 100%;">
    <div class="badge">ACL 2025</div>
    <img src='images/4.png' alt="sym" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>
 
### Abstract

Recent advances in large language models (LLMs) have significantly improved multi-hop question answering (QA) through direct Chain-of-Thought (CoT) reasoning. However, the irreversible nature of CoT leads to error accumulation, making it challenging to correct mistakes in multi-hop reasoning. This paper introduces ReAgent: Reversible multi-Agent collaborative framework augmented with explicit backtracking mechanisms, enabling reversible multi-hop reasoning. By incorporating text-based retrieval, information aggregation and validation, our system can detect and correct errors mid-reasoning, leading to more robust and interpretable QA outcomes. The framework and experiments serve as a foundation for future work on error-tolerant QA systems. Empirical evaluations across three benchmarks indicate ReAgent's efficacy, yielding average about 6% improvements against baseline models.

---

## **Adaptive Interruption and Trust-Weighted Voting for Secure Multi-Agent Collaboration in Complex Question Answering**

**Authors:** **Ying Zhu\***, Zhao Xinjie, Irene Li
 
### Abstract

Complex question answering often demands reasoning over multiple sources of information and integrating diverse forms of knowledge. However, reliance on a single chain-of-thought can lead to the propagation of errors, and systems remain vulnerable to malicious or misleading inputs. In this paper, we propose an enhanced multi-agent framework that introduces a fine-grained interruption (``breakpoint'') mechanism and a dynamic trust-weighted voting strategy to improve both robustness and explainability in multi-hop QA. Our approach integrates Bayesian-inspired agent credibility updates, segment-by-segment answer generation, and a mathematically grounded interruption strategy to limit error propagation. We describe the theoretical underpinnings and practical workflow of our system, then demonstrate how interruption triggers, weighted voting, and multi-agent collaboration converge to produce more accurate and secure answers. Experiments on benchmark QA datasets confirm significant improvements in correctness, stability, and interpretability, showing promise for broader adoption in adversarial or high-stakes settings.
 
---



# 📖 Educations
- *2022.09 - 2025.03 (now)*, the School of Artificial Intelligence, Nanjing University of Information Science and Technology.

---

# 💻 Internships
- *2024.10 - 2025.03 (now)*, Internship, Shanghai Artificial Intelligence Laboratory ([Shanghai AI Lab](https://www.shlab.org.cn/ "上海人工智能实验室")), China.
- *2024.11 - 2025.03 (now)*, Research Assistant, The University of Tokyo, Japan.
- *2025.01 - 2025.03 (now)*, Research Assistant, Science and Technology Bureau of Mengzi City, Honghe Prefecture, Yunnan Province, China **(State-owned enterprise)**.
