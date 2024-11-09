from src.visualize import visualize_distribution
from src.download import download_dataset

if __name__ == "__main__":
    download_dataset()
    visualize_distribution('data')
