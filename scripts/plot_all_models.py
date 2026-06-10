from src.evaluation.model_comparison import plot_model_comparison

results = {
    "ssd": {"precision": 0.7417, "recall": 0.4885, "mAP50": 0.7675},
    "faster_rcnn": {"precision": 0.6722, "recall": 0.8450, "mAP50": 0.9239},
    "yolov8n": {"precision": 0.5025, "recall": 0.3613, "mAP50": 0.3807},
    "yolov11n": {"precision": 0.5086, "recall": 0.2812, "mAP50": 0.3380},
    "yolov26": {"precision": 0.6551, "recall": 0.5944, "mAP50": 0.6194},
    "detr": {"precision": None, "recall": None, "mAP50": None}
}

plot_model_comparison(results)