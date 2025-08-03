# Pneumonia Detection from Chest X-rays 🫁

A full-stack web application that detects pneumonia from chest X-ray images using a Convolutional Neural Network (CNN). Built with Flask, TensorFlow, HTML/CSS/JS, and runs locally on macOS or any machine with Python.

---

## 🚀 Features

- Upload chest X-ray images via web interface
- Predicts if the patient has **Pneumonia** or is **Normal**
- Uses a trained CNN model (`.h5`) for image classification
- Real-time predictions with confidence scores
- Clean UI built with HTML/CSS and JavaScript
- Lightweight backend with Flask (no PHP/XAMPP needed)

---

## 🖥️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **ML Model:** TensorFlow/Keras (CNN)
- **Deployment:** Run locally using virtualenv (no XAMPP)

---

## 📦 Folder Structure

pneumonia_flask_app/
│
├── app.py # Flask app
├── model/
│ └── model.h5 # Trained CNN model
├── static/
│ └── style.css # Frontend styling
├── templates/
│ └── index.html # HTML UI
├── uploads/ # Temp uploaded images
├── venv/ # Python virtual environment
└── README.md # You're here!

---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/msp2946-ss/pneumonia_flask_app.git
cd pneumonia_flask_app

### 2. Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

-- pip install flask tensorflow pillow
💡 If you're using macOS and get a "externally-managed-environment" error, use a virtual environment like above.

### 4. Add Trained Model
Place your model.h5 file in the model/ folder.
You can train your own CNN or use a pre-trained one (recommended: trained on ChestX-ray8).

### 5. Run the App

python app.py
Then open your browser at:
http://localhost:5000

### 📸 Screenshots
url not available.

### 🛡 Disclaimer
This project is for educational purposes only. It is not approved for clinical or diagnostic use.

### 📬 Contact
For questions or collaboration:

GitHub: msp2946-ss









Ask ChatGPT
