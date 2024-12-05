from emotion_detection import emotion_detector

def test_emotion_detection():
    test_cases = [
        ("Me alegra que esto haya sucedido", "joy"),
        ("Estoy realmente enojado por esto", "anger"),
        ("Me siento disgustado solo de oír sobre esto", "disgust"),
        ("Estoy tan triste por esto", "sadness"),
        ("Tengo mucho miedo de que esto suceda", "fear"),
        ("", None),
    ]

    for text, expected in test_cases:
        result = emotion_detector(text)
        assert result['dominant_emotion'] == expected, f"Error: {text}"

if __name__ == "__main__":
    test_emotion_detection()
    print("Todas las pruebas pasaron correctamente.")
