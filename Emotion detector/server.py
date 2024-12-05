from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Texto inválido. ¡Por favor, inténtalo de nuevo!"}), 400
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
