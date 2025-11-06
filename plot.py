import matplotlib.pyplot as plt
import numpy as np

def plot_eval_results(models, datasets, scores, title="Model Comparison"):
    colors = ["#A6CE83", "#5DAA8A", "#3C5873", "#C5D6F0"]

    num_datasets = len(datasets)
    num_models = len(models)
    width = 0.18  # 每个柱子的宽度
    group_gap = 0.35  # 控制组间的间距

    # 计算每组的中心位置
    x = np.arange(num_datasets) * (num_models * width + group_gap)

    plt.figure(figsize=(12, 6), dpi=360)

    # 网格线在柱子下方
    plt.grid(axis='y', color="#E0E0E0", linestyle='-', linewidth=0.8, zorder=0)

    # 绘制柱状图
    for i, (model, model_scores) in enumerate(zip(models, scores)):
        plt.bar(x + i * width, model_scores, width,
                label=model, color=colors[i % len(colors)],
                edgecolor="#D0D0D0", zorder=3)

    # 坐标轴与文字设置
    plt.xticks(x + (num_models - 1) * width / 2, datasets, rotation=30, ha='center', fontsize=11)
    plt.ylabel("Score", fontsize=12)
    plt.ylim(5, 105)
    plt.title(title, fontsize=14, weight='bold', pad=20)

    # 边框颜色设置为灰色
    ax = plt.gca()
    for spine in ax.spines.values():
        spine.set_color("#BEBEBE")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # 图例放在上方
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.06),
               ncol=len(models), frameon=False, fontsize=10)

    plt.tight_layout()
    plt.savefig("./static/images/accuracy.png", dpi=300)


if __name__ == "__main__":
    models = ["Qwen2.5-Math-7B-Instruct", "SDAR-8B-Chat", "Trado-8B-Instruct", "Aha-Math-8B-Instruct(ours)"]
    datasets = ["MATH500", "GSM8K", "AIME2024", "AIME2025"]
    scores = [
        [72.21, 91.96, 5.63, 3.96],
        [71.85, 89.87, 9.17, 9.38],
        [75.59, 91.06, 11.67, 15.00],
        [82.37, 94.00, 13.00, 16.00],
    ]

    plot_eval_results(models, datasets, scores, title="Accuracy")
