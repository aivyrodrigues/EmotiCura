import os
import requests
from dotenv import load_dotenv

# Load Hugging Face API token from .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Define the Hugging Face Inference API endpoint and headers
API_URL = "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def detect_emotion(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code != 200:
        return "Unknown", 0.0

    result = response.json()

    if result and isinstance(result[0], list):
        top_emotion = result[0][0]
        return top_emotion['label'].capitalize(), round(top_emotion['score'] * 100, 2)
    else:
        return "Unknown", 0.0

# Function to query the Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()  # Raise error if request failed
    return response.json()

# Main logic
if __name__ == "__main__":
    text = input("How are you feeling today? ")
    result = query({"inputs": text})

    if result and isinstance(result[0], list):
        top_emotion = result[0][0]
        label = top_emotion['label']
        score = top_emotion['score']
        print(f"Detected Emotion: {label.capitalize()} (Confidence: {score:.2f})")
    else:
        print("Unable to detect emotion. Please try again.")
