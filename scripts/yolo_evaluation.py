"""
Evaluate YOLOv8 model on validation/test set
"""

from ultralytics import YOLO

# Path to trained weights
MODEL_PATH = "models/ev_yolo_train/weights/best.pt"

# Dataset YAML
DATA_YAML = "dataset/data.yaml"

def evaluate_yolo():
    # Load model
    model = YOLO(MODEL_PATH)

    # Run evaluation
    metrics = model.val(data=DATA_YAML)

    print("Evaluation completed.")
    print(metrics)  # precision, recall, mAP50, mAP50-95

if __name__ == "__main__":
    evaluate_yolo()