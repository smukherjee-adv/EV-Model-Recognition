import os
import cv2
import albumentations as A
from tqdm import tqdm
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# === Folder structure ===
input_base = "/content/drive/MyDrive/ev_new_sorted"           # Your actual images
output_base = "/content/drive/MyDrive/ev_augmented_data"      # Where augmented data will go
os.makedirs(output_base, exist_ok=True)

# === Augmentation simulating real conditions ===
transform = A.Compose([
    A.RandomBrightnessContrast(p=0.5),
    A.MotionBlur(blur_limit=3, p=0.3),
    A.RandomShadow(p=0.4),
    A.RandomFog(p=0.2),
    A.Rotate(limit=25, p=0.5),
    A.HorizontalFlip(p=0.5),
    A.RandomScale(scale_limit=0.2, p=0.3),
    A.Perspective(scale=(0.05, 0.1), p=0.4),
    A.GaussNoise(p=0.3),
])

image_count = 0

# === Walk through subfolders ===
for root, dirs, files in os.walk(input_base):
    rel_path = os.path.relpath(root, input_base)
    output_folder = os.path.join(output_base, rel_path)
    os.makedirs(output_folder, exist_ok=True)

    for filename in tqdm(files, desc=f" Processing {rel_path}", leave=False):
        file_path = os.path.join(root, filename)
        image = cv2.imread(file_path)

        if image is None:
            print(f" Skipped unreadable image: {file_path}")
            continue

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        for i in range(3):  # Generate 3 augmented copies
            augmented = transform(image=image)['image']
            aug_name = f"aug_{i}_{filename}"
            aug_path = os.path.join(output_folder, aug_name)
            cv2.imwrite(aug_path, cv2.cvtColor(augmented, cv2.COLOR_RGB2BGR))
            image_count += 1

print(f"\n Augmented {image_count} images saved to: {output_base}")
