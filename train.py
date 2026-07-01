import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
data = pd.read_csv("data/emails.csv")

# Features and labels
X = data["text"]
y = data["label"]

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, "model/phishing_detector.pkl")

print("✅ Model trained successfully!")