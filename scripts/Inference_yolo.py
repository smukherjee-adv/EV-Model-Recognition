"""
Run YOLOv8 inference on images and save outputs
"""

from ultralytics import YOLO
import os
import cv2

# Paths
MODEL_PATH = "models/ev_yolo_train/weights/best.pt"
INPUT_DIR = "dataset/test_images"       # folder of test images
OUTPUT_DIR = "yolo_outputs"             # folder for saving predictions

def run_inference():
    # Create output folder
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load model
    model = YOLO(MODEL_PATH)

    # Predict on folder
    results = model.predict(
        source=INPUT_DIR,
        conf=0.25,
        save=True,
        project=OUTPUT_DIR,
        name="detections"
    )

    print("Inference completed. Results saved to:", os.path.join(OUTPUT_DIR, "detections"))

if __name__ == "__main__":
    run_inference()