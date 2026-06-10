import json
import os
import matplotlib.pyplot as plt
import numpy as np


def plot_model_comparison(path="results/metrics/all_models.json"):
    with open(path, "r") as f:
        data = json.load(f)

    models = list(data.keys())

    precision = [data[m]["precision"] for m in models]
    recall = [data[m]["recall"] for m in models]
    map50 = [data[m]["mAP50"] for m in models]

    x = np.arange(len(models))
    width = 0.25

    plt.figure(figsize=(12, 6))

    # bars
    plt.bar(x - width, precision, width, label="Precision")
    plt.bar(x, recall, width, label="Recall")
    plt.bar(x + width, map50, width, label="mAP@50")

    plt.xticks(x, models, rotation=20)
    plt.ylim(0, 1.0)

    plt.title("Model Comparison (Precision / Recall / mAP@50)", fontsize=14)
    plt.ylabel("Score")

    plt.grid(axis="y", alpha=0.3)
    plt.legend()

    os.makedirs("results/plots", exist_ok=True)
    save_path = "results/plots/model_comparison.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    print(f"Saved to: {save_path}")