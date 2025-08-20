# Download EV images using car dataset excel file and icrawler
# Install required packages
!pip install icrawler pandas openpyxl

# Import necessary modules
import os
import pandas as pd
from icrawler.builtin import GoogleImageCrawler
from google.colab import files

# === CONFIG ===
IMAGES_PER_MODEL = 5 # can be increased
SEARCH_SUFFIX = " electric car"
OUTPUT_DIR = "ev_images_1"

# === UPLOAD FILE ===
uploaded = files.upload()

# Get the uploaded file name
for filename in uploaded.keys():
    excel_path = filename
    break

# === Clean folder name ===
def clean_folder_name(name):
    return name.replace(" ", "_").replace("/", "_")

# === Download images ===
def download_images(query, save_path, max_num):
    crawler = GoogleImageCrawler(storage={"root_dir": save_path})
    crawler.crawl(keyword=query, max_num=max_num)

# === Read Excel file ===
df = pd.read_excel(excel_path)  # This is the key fix!

if df.shape[1] < 2:
    raise ValueError("Excel must have at least two columns: Brand, Model")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Download images for each car ===
for idx, row in df.iterrows():
    brand = str(row[0]).strip()
    model = str(row[1]).strip()
    query = f"{brand} {model}{SEARCH_SUFFIX}"

    folder_name = clean_folder_name(f"{brand}_{model}")
    save_path = os.path.join(OUTPUT_DIR, folder_name)

    print(f"[{idx+1}] Downloading images for: {query}")
    os.makedirs(save_path, exist_ok=True)
    download_images(query, save_path, IMAGES_PER_MODEL)

print("All images downloaded.")
