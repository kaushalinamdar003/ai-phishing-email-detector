import joblib

# Load the trained model
model = joblib.load("model/phishing_detector.pkl")

print("===== AI Phishing Email Detector =====")

while True:
    email = input("\nEnter an email (or type 'exit' to quit): ")

    if email.lower() == "exit":
        print("Goodbye!")
        break

    prediction = model.predict([email])[0]

    print("\nPrediction:", prediction)