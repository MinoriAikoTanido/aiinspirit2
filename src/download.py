import os
import requests
from tqdm import tqdm

def download_dataset():
    dataset_path = "data/archive.zip"
    url = "https://www.kaggle.com/api/v1/datasets/download/uwrfkaggler/ravdess-emotional-speech-audio"
    
    # Check if the dataset already exists
    if os.path.exists(dataset_path):
        print("Dataset already exists. Skipping download.")
        return
    
    print("Dataset not found. Downloading...")
    
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(dataset_path), exist_ok=True)
    
    # Stream the download and add a progress bar
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check if the request was successful

    # Get the total file size
    total_size = int(response.headers.get("content-length", 0))
    
    # Download the file with progress bar
    with open(dataset_path, "wb") as file, tqdm(
        desc="Downloading",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
            progress_bar.update(len(chunk))
    
    print("Download complete.")
