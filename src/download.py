
import os
import subprocess

def download_dataset():
    """
    Checks if the 'data/' directory exists, and if it does, clones the dataset from
    the GitHub repository into this directory.
    """
    data_dir = "data/"
    repo_url = "https://github.com/MinoriAikoTanido/aiinspirit2.git"

    # Check if the 'data/' directory exists
    if os.path.exists(data_dir):
        # Clone the repository into the 'data/' directory
        try:
            print(f"Downloading dataset into {data_dir}...")
            subprocess.run(["git", "clone", repo_url, data_dir], check=True)
            print("Dataset downloaded successfully.")
        except subprocess.CalledProcessError:
            print("Failed to download the dataset.")
    else:
        print(f"The directory '{data_dir}' does not exist. Please create it first.")
