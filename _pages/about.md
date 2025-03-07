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
 
I am currently an junior undergraduate student at the School of Artificial Intelligence, Nanjing University of Information Science and Technology, where I am fortunate to be advised by [Peilan Xu](https://scholar.google.ca/citations?hl=zh-CN&user=MYTn5zYAAAAJ "许沛澜"). 

My current research focuses on evolutionary computation, LLM reasoning, multi-agent frameworks, and various LLM application research. Several papers have been submitted to the top journals and conferences in the field of artificial intelligence (such as ACM Transactions, IJCAI, ACL ...), and my representative work "Density-Assisted Evolutionary Dynamic Multimodal Optimization" has been accepted by ACM TELO.

Currently, I am undertaking an internship at [Shanghai AI Lab](https://www.shlab.org.cn/ "上海人工智能实验室") under the mentorship of [Rui Su](https://scholar.google.ca/citations?hl=zh-CN&authuser=2&user=tLLmRBwAAAAJ "苏锐"). Concurrently, I am working as a research assistant to [Irene Li](https://scholar.google.com/citations?hl=zh-CN&user=JuYPjCMAAAAJ&view_op=list_works&sortby=pubdate) in [Matsuo Lab](https://weblab.t.u-tokyo.ac.jp/) and collaborate with [Xinjie Zhao]([https://openreview.net/profile?id=~Zhao_Xinjie1](https://scholar.google.com/citations?hl=zh-CN&user=_l5fPvEAAAAJ) "赵新杰") closely.

I am honoured to be recognized as a **Kaggle Expert** for winning two silver medals in LLM competitions. Additionally, I won the championship in the [IEEE CEC Competition on Seeking Multiple Optima in Dynamic Environments](http://mi.hitsz.edu.cn/activities/smode_cec2023/index.html) for two consecutive years (2023,2024), and was awarded a national first prize in the Lanqiao Cup.

I am actively seeking opportunities for academic collaboration and would be delighted to discuss potential partnerships. Please feel free to contact me at <auraithm@gmail.com> (personal email) or <evonexusx@gmail.com>.


# 🔥 News
- *2025.03*: &nbsp;🎉🎉 Paper "Density-Assisted Evolutionary Dynamic Multimodal Optimization" is accepted by **ACM Transactions on Evolutionary Learning and Optimization**.
- *2025.03*: &nbsp;🎉🎉 Won a silver medal at Kaggle competitions "LLMs - You Can't Please Them All".

# 🎖 Honors and Awards
- *2025.03* Won a silver medal at the Kaggle competition **"LLMs - You Can't Please Them All"**.
- *2024.07* Won the championship in the **IEEE CEC 2024 Competition on Seeking Multiple Optima in Dynamic Environments**.
- *2024.06* Won the national first prize in the Lanqiao Cup.
- *2024.04* Won a silver medal at the Kaggle competition **"LLM Prompt Recovery"**.
- *2023.07* Won the championship in the **IEEE CEC 2023 Competition on Seeking Multiple Optima in Dynamic Environments**.

# 📝 Publications 
- **Density-Assisted Evolutionary Dynamic Multimodal Optimization**, **YingZhu**, Peilan Xu, Jiahao Huang, Xin Lin, Wenjian Luo, **ACM TELO**.
- **[GRATR: Zero-Shot Evidence Graph Retrieval-Augmented Trustworthiness Reasoning](https://arxiv.org/abs/2408.12333)**, **Ying Zhu\***, Shengchang Li\*, Ziqian Kong, Qiang Yang, Peilan Xu, **arXiv**.
- **[Narrative-Driven Travel Planning: Geocultural-Grounded Script Generation with Evolutionary Itinerary Optimization](https://arxiv.org/abs/2502.14456)**, Ran Ding\*, Ziyu Zhang\*, **Ying Zhu\***, Ziqian Kong, Peilan Xu, **arXiv**.
- **ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA**, Zhao Xinjie, Fan Gao, Rui Yang, Yingjian Chen, Yuyang Wang, **Ying Zhu**, Jiacheng Tang, Irene Li , **arXiv**.


# 💬 Research Overviews
<div style="float: left; margin-right: 20px; width: 30%;">
    <div class="badge">ACM TELO</div>
    <img src='images/Density_0.png' alt="sym" width="200%">
</div>

**Density-Assisted Evolutionary Dynamic Multimodal Optimization**

**YingZhu**, Peilan Xu, Jiahao Huang, Xin Lin, Wenjian Luo

**Journal: ACM Transactions on Evolutionary Learning and Optimization**

**Abstract**
Dynamic multimodal optimization problems (DMMOPs) demand algorithms capable of swiftly locating and tracking multiple optimal solutions over time. The primary challenge lies in controlling the population diversity to facilitate effective exploration, all within the limitation of computational resources between consecutive environmental changes. In this paper, we study the utilization of density information derived from both current and historical populations to enhance exploration. First, for each active sub-population, we construct a density landscape based on the distribution of concurrently active sub-populations, and establish dominance relationships between candidate solutions in the sub-population based on density and fitness values, directing this sub-population towards exploring low-density promising areas. Then, for each converged sub-population, we construct a density landscape based on the distribution of sub-populations that have historically become extinct, guiding the restart of this sub-population in low-density unexploited areas. Finally, we develop a comprehensive framework of density-assisted evolutionary algorithm (DAEA), which encompasses density-assisted search and restart, also combined with initialization. Moreover, we employ prediction and memory strategies to enhance the performance of DAEA in dynamic environments. Notably, the algorithm relies on an external monitor to detect environmental changes and trigger the dynamic response strategy. DAEA is tested on the CEC'2022 dynamic multimodal optimization benchmark suite, and is compared against several state-of-the-art dynamic multimodal optimization algorithms. The experimental results demonstrate the competitiveness of DAEA in handling DMMOPs.



# 📖 Educations
- *2022.09 - 2025.03 (now)*, the School of Artificial Intelligence, Nanjing University of Information Science and Technology.

# 💻 Internships
- *2024.10 - 2025.03 (now)*, Internship, Shanghai Artificial Intelligence Laboratory ([Shanghai AI Lab](https://www.shlab.org.cn/ "上海人工智能实验室")), China.
- *2024.11 - 2025.03 (now)*, Research Assistant, Matsuo-Iwasawa Lab ([Matsuo Lab](https://weblab.t.u-tokyo.ac.jp/)), Japan.
- *2025.01 - 2025.03 (now)*, Research Assistant, Science and Technology Bureau of Mengzi City, Honghe Prefecture, Yunnan Province, China **(State-owned enterprise)**.
