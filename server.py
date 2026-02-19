from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotiondetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print(response)
    if response is not None:
        label = response['dominant_emotion']
        print(label)
    # Using an f-string for cleaner formatting
        return f"For the given statement, the system response is {response}. The dominant emotion is {label}."
    else:
         return "Invalid text! Please try again!"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)