# **Emotion Detection Web App - Final project**

A modern web application that analyzes text input to detect and display emotions like **joy**, **anger**, **sadness**, and more. Built using **Flask**, **Bootstrap**, and IBM Watson's Emotion Detection API. 

<div align="center"> <img src="https://th.bing.com/th/id/OIP.4AUfRt3_caScoF7zvKA7eAHaDt?rs=1&pid=ImgDetMain" alt="Emotion Detection Image" width="80%"/> </div>

---

## ✨ **Features**
- 🎯 **Real-time Emotion Analysis**: Detects emotions such as:
  - Joy 😊
  - Anger 😡
  - Sadness 😢
  - Fear 😱
  - Disgust 🤢
- 🛠️ **User-Friendly Interface**: Clean and intuitive UI built with **Bootstrap**.
- 🔒 **Error Handling**: Handles invalid inputs with graceful error messages.
- 🚀 **Lightweight Backend**: Powered by **Flask** for fast responses.

---

## ⚡ **Getting Started**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/emotion-detection-web-app.git
cd emotion-detection-web-app
```

### **2️⃣ Set Up Your Environment**
- **Linux/macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
python server.py
```

### **5️⃣ Open Your Browser**
Visit the app at:
```
http://localhost:5000
```

---

## 🏗️ **Project Structure**
```plaintext
emotion-detection-web-app/
│
├── templates/
│   └── index.html                       # Frontend UI
├── static/
│   └── mywebscript.js                   # JavaScript for client-side logic
├── emotion_detection.py                 # Core logic using IBM Watson API
├── server.py                            # Flask server
├── test_emotion_detection.py            # Unit tests
├── requirements.txt                     # Dependencies
└── README.md                            # Project documentation
```

---

## 🌍 **How It Works**
1. **Input**: Enter text in the input field (e.g., "I love this app!").
2. **Analyze**: Click on "Run Sentiment Analysis".
3. **Output**: View the emotion scores and the dominant emotion.

---

## 🔬 **Unit Testing**
To ensure reliability, unit tests are included. Run them with:
```bash
python test_emotion_detection.py
```
You should see output like:
```
All tests passed successfully!
```

---

## ❗ **Error Handling**
- **Empty Input**: Displays a user-friendly error message.
- **Invalid API Response**: Notifies the user of issues with processing.

---

## 📋 **API Details**
### **Endpoint**
- **Route**: `/emotionDetector`
- **Method**: `GET`
- **Parameter**: `textToAnalyze` (string)
- **Response**: 
```json
{
  "anger": 0.01,
  "disgust": 0.05,
  "fear": 0.10,
  "joy": 0.70,
  "sadness": 0.14,
  "dominant_emotion": "joy"
}
```

---

## 🤝 **Contributing**
We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

---

## 📜 **License**
This project is licensed under the [Apache License](LICENSE). Feel free to use and modify it.

---

## ❤️ **Acknowledgments**
- **IBM Watson** for their robust NLP API.
- **Flask** and **Bootstrap** for making development efficient.
- Icons from [Twemoji](https://twemoji.twitter.com/).

---
