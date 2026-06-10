import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.metrics import precision_recall_curve, confusion_matrix, ConfusionMatrixDisplay


# =========================
# PR CURVE
# =========================
def plot_pr_curve(scores, labels):
    os.makedirs("results/plots", exist_ok=True)

    precision, recall, _ = precision_recall_curve(labels, scores)

    plt.figure()
    plt.plot(recall, precision)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")

    plt.savefig("results/plots/pr_curve.png", dpi=300, bbox_inches="tight")
    plt.show()


# =========================
# CONFUSION MATRIX
# =========================
def plot_confusion_matrix(y_true, y_pred, class_names):
    os.makedirs("results/plots", exist_ok=True)

    cm = confusion_matrix(y_true, y_pred)

    disp = ConfusionMatrixDisplay(cm, display_labels=class_names)
    disp.plot(xticks_rotation=45)

    plt.title("Confusion Matrix")

    plt.savefig("results/plots/confusion_matrix.png", dpi=300, bbox_inches="tight")
    plt.show()