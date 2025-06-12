from flask import Blueprint, render_template, request
from .emotion import detect_emotion

# Define a Blueprint named 'main'
main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    emotion = None
    confidence = None

    if request.method == 'POST':
        user_input = request.form.get('text', '')
        emotion, confidence = detect_emotion(user_input)

    return render_template('index.html', emotion=emotion, confidence=confidence)
