# src/visualize.py

import os
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

# Function to parse metadata from filenames
def parse_filename(filename):
    parts = filename.split("-")
    return {
        "modality": parts[0],
        "vocal_channel": parts[1],
        "emotion": parts[2],
        "intensity": parts[3],
        "statement": parts[4],
        "repetition": parts[5],
        "actor": parts[6].split(".")[0]
    }

# Function to visualize the distribution
def visualize_distribution(dataset_path):
    # Ensure the plots directory exists
    os.makedirs("data/plots", exist_ok=True)
    
    # Gather data from all files in the directory
    data = []
    for root, dirs, files in os.walk(dataset_path):
        for file in tqdm(files, desc="Processing files"):
            if file.endswith(".wav"):
                metadata = parse_filename(file)
                data.append(metadata)
                
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    
    # Visualize distribution of emotions
    plt.figure(figsize=(10, 6))
    df['emotion'].value_counts().sort_index().plot(kind='bar')
    plt.title("Distribution of Emotions")
    plt.xlabel("Emotion")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.savefig("data/plots/emotion_distribution.png")
    plt.close()
    
    # Visualize distribution of intensity levels
    plt.figure(figsize=(10, 6))
    df['intensity'].value_counts().sort_index().plot(kind='bar')
    plt.title("Distribution of Intensity Levels")
    plt.xlabel("Intensity")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.savefig("data/plots/intensity_distribution.png")
    plt.close()
    
    # Visualize distribution across actors
    plt.figure(figsize=(10, 6))
    df['actor'].value_counts().sort_index().plot(kind='bar')
    plt.title("Distribution Across Actors")
    plt.xlabel("Actor ID")
    plt.ylabel("Count")
    plt.xticks(rotation=90)
    plt.savefig("data/plots/actor_distribution.png")
    plt.close()
