"""
Train YOLOv8 on custom EV dataset
"""

from ultralytics import YOLO
import os

# Paths
DATA_YAML = "dataset/data.yaml"   # dataset config (images + labels defined here)
MODEL_NAME = "yolov8n.pt"         # starting checkpoint
OUTPUT_DIR = "models"             # folder to save trained models

def train_yolo():
    # Load YOLOv8 model
    model = YOLO(MODEL_NAME)

    # Train
    model.train(
        data=DATA_YAML,
        epochs=50,
        imgsz=640,
        batch=16,
        project=OUTPUT_DIR,
        name="ev_yolo_train",
        device=0  # 0 = GPU, "cpu" = CPU
    )

    print("Training completed. Check models/ev_yolo_train/ for weights.")

if __name__ == "__main__":
    train_yolo()