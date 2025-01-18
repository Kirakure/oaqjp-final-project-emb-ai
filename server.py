from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():    
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    anger = response['anger']
    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is anger: {anger}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)