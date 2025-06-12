# EmotiCura – AI-Powered Mental Health Companion

EmotiCura is a lightweight Flask-based web app that uses a Hugging Face NLP model to detect emotions from user-inputted text.

## Features
- Takes user input via a form
- Sends the input to a Hugging Face model via API
- Returns detected emotion and confidence

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/EmotiCura.git
    cd EmotiCura
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # or venv\\Scripts\\activate on Windows
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Add your Hugging Face API key in a `.env` file:
    ```
    HUGGINGFACE_API_TOKEN=your_token_here
    ```

5. Run the app:
    ```
    python run.py
    ```

## License
MIT
