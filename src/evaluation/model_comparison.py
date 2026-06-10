import matplotlib.pyplot as plt
import os


def plot_model_comparison(results):
    os.makedirs("results/plots", exist_ok=True)

    models = list(results.keys())
    mAP = [results[m]["mAP50"] for m in models]
    precision = [results[m]["precision"] for m in models]
    recall = [results[m]["recall"] for m in models]

    x = range(len(models))

    plt.figure(figsize=(12, 6))

    plt.bar(x, mAP, label="mAP@0.5")
    plt.bar(x, precision, alpha=0.6, label="Precision")
    plt.bar(x, recall, alpha=0.4, label="Recall")

    plt.xticks(x, models)
    plt.title("Model Comparison (Object Detection)")
    plt.legend()

    save_path = "results/plots/model_comparison.png"
    plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()