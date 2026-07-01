📧 AI Phishing Email Detector

An AI-based machine learning project that detects whether an email is phishing or legitimate using Natural Language Processing (NLP) and a trained classification model.

🚀 Features
Detects phishing emails using text analysis
Trained on labeled email dataset (spam / ham or phishing / safe)
Uses NLP preprocessing (cleaning, vectorization)
Machine Learning classification model (e.g., Naive Bayes / Logistic Regression)
Simple Python-based pipeline
Easy to run and extend
🛠️ Tech Stack
Python 🐍
Pandas
Scikit-learn
NumPy
NLTK / Regex (for text cleaning)
Jupyter Notebook (optional)


📁 Project Structure
ai-phishing-email-detector/
│
├── data/
│   └── emails.csv
│
├── model/
│   └── trained_model.pkl
│
├── train.py
├── predict.py
├── app.py (optional)
├── requirements.txt
└── README.md
📊 Dataset

The dataset should contain email text and labels:

text	label
"Your account is locked..."	phishing
"Meeting scheduled tomorrow"	safe

File location:

data/emails.csv


⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/ai-phishing-email-detector.git
cd ai-phishing-email-detector

2. Create virtual environment
python -m venv venv

3. Activate environment

Windows (PowerShell):

venv\Scripts\Activate.ps1

Windows (CMD):

venv\Scripts\activate.bat
4. Install dependencies
pip install -r requirements.txt
▶️ Run the Project
Train model
python train.py
Predict email
python predict.py
🧠 How It Works
Load dataset (emails.csv)
Clean and preprocess text (remove stopwords, punctuation, etc.)
Convert text into numeric format using TF-IDF / CountVectorizer
Train ML model
Save trained model
Predict new email as phishing or safe
📌 Example Output
Input: "Your bank account has been suspended. Click here."
Prediction: PHISHING ⚠️
⚠️ Common Issues
❌ FileNotFoundError

Make sure dataset is placed correctly:

data/emails.csv
❌ venv activation error

Run:

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
📈 Future Improvements
Add deep learning model (LSTM / BERT)
Web dashboard using Flask / Streamlit
Email API integration
Real-time phishing detection
👨‍💻 Author
Kaushal Inamdar
AI / Cybersecurity Project