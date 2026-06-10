import argparse
import json
import os
from datetime import datetime

from src.evaluation.model_comparison import plot_model_comparison

from src.utils.utils import set_seed

set_seed(42)

# =========================
# ARGUMENTS
# =========================
parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, required=True)
args = parser.parse_args()

model_name = args.model


# =========================
# METRICS DATABASE (пока ручной вариант)
# =========================
metrics_db = {
    "ssd": {
        "precision": 0.7417,
        "recall": 0.4885,
        "mAP50": 0.7675
    },
    "faster_rcnn": {
        "precision": 0.6722,
        "recall": 0.8450,
        "mAP50": 0.9239
    },
    "yolov8n": {
        "precision": 0.5025,
        "recall": 0.3613,
        "mAP50": 0.3807
    },
    "yolov11n": {
        "precision": 0.5086,
        "recall": 0.2812,
        "mAP50": 0.3380
    },
    "detr": {
        "precision": None,
        "recall": None,
        "mAP50": None
    }
}


# =========================
# CHECK
# =========================
if model_name not in metrics_db:
    raise ValueError(f"Unknown model: {model_name}")


os.makedirs("results/plots", exist_ok=True)
os.makedirs("results", exist_ok=True)
os.makedirs("logs", exist_ok=True)


# =========================
# SAVE METRICS
# =========================
metrics = metrics_db[model_name]

with open("results/metrics.json", "w") as f:
    json.dump({
        "model": model_name,
        **metrics
    }, f, indent=4)


# =========================
# LOG
# =========================
with open("logs/run.log", "a") as f:
    f.write(f"{datetime.now()} | {model_name}\n")


print("\nModel:", model_name)
for k, v in metrics.items():
    print(f"{k}: {v}")

print("\nDone.")


# =========================
# GLOBAL PLOT (ВАШ ГЛАВНЫЙ ГРАФИК)
# =========================
all_results = {
    "ssd": metrics_db["ssd"],
    "faster_rcnn": metrics_db["faster_rcnn"],
    "yolov8n": metrics_db["yolov8n"],
    "yolov11n": metrics_db["yolov11n"]
}

plot_model_comparison(all_results)