from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    data = request.json
    text = data.get("text", "")
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Texto inválido. ¡Por favor, inténtalo de nuevo!"}), 400
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
