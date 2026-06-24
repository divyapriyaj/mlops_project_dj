from huggingface_hub import login
from datasets import load_dataset
import os

# Get token from GitHub Actions
token = os.getenv("HF_TOKEN")

# Login to Hugging Face
login(token=token)

# Example dataset (replace with your real dataset later)
dataset = load_dataset("imdb")

# Push dataset to Hugging Face Hub
dataset.push_to_hub("Priya14Divya/tourism-wellness-dataset")
