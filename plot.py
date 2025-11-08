import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import os

def draw_perfect_round_bar(ax, x_left, width, height, radius, color):
    """
    顶部两个角圆角，不被竖线覆盖
    """
    r = min(radius, width / 2)

    verts = [
        (x_left, 0),                      # 1 左下
        (x_left, height - r),            # 2 左侧竖线（圆角下方）
        (x_left, height),                # 3 左上圆角控制点1
        (x_left + r, height),            # 4 左上圆角控制点2
        (x_left + width - r, height),    # 5 顶部直线
        (x_left + width, height),        # 6 右上圆角控制点1
        (x_left + width, height - r),    # 7 右上圆角控制点2
        (x_left + width, 0),             # 8 右侧竖直到底
        (x_left, 0)                      # 9 回到左下
    ]

    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.CURVE3,
        Path.CURVE3,
        Path.LINETO,
        Path.CURVE3,
        Path.CURVE3,
        Path.LINETO,
        Path.CLOSEPOLY
    ]

    patch = PathPatch(Path(verts, codes), facecolor=color, edgecolor="none")
    ax.add_patch(patch)

def plot_eval_results(models, datasets, scores):
    colors = ["#395FA8", "#6FA8DC", "#5290C8", "#5DD4D0"]
    num_datasets = len(datasets)
    num_models = len(models)

    width = 0.18
    gap = 0.05
    group_gap = 0.6

    x_center = np.arange(num_datasets) * (num_models * (width + gap) + group_gap) + 0.3

    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

    # 绘制圆角柱子
    for i, (_, vals) in enumerate(zip(models, scores)):
        for j, y in enumerate(vals):
            x = x_center[j] + i * (width + gap)
            draw_perfect_round_bar(ax, x, width, y, radius=width * 0.5, color=colors[i % len(colors)])

    # X轴设置
    ax.set_xticks(x_center + (num_models - 1) * (width + gap) / 2)
    ax.set_xticklabels(datasets, fontsize=12)

    # ✅ 防止最右边柱子被裁剪
    ax.set_xlim(-0.2, x_center[-1] + num_models * (width + gap) + 0.3)

    # 其他设置
    ax.set_ylabel("Accuracy", fontsize=14)
    ax.set_ylim(0, 105)

    ax.legend(models, loc="upper center", bbox_to_anchor=(0.5, 1.06),
              ncol=len(models), frameon=False)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()

    out_path = "./static/images/accuracy.svg"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    plt.savefig(out_path, format="svg")
    plt.close()

if __name__ == "__main__":
    models = ["Qwen2.5-7B-Instruct", "SDAR-8B-Chat", "Trado-8B-Instruct", "Aha-8B-Instruct (ours)"]
    datasets = ["MATH500", "GSM8K", "AIME2024", "AIME2025", "OlympiadBench"]
    scores = [
        [73.78, 89.78, 8.96, 5.63, 36.58],
        [71.85, 89.87, 9.17, 9.38, 36.03],
        [75.59, 91.06, 11.67, 15.00, 40.32],
        [81.60, 90.65, 20.00, 19.17, 44.81]
    ]
    plot_eval_results(models, datasets, scores)
