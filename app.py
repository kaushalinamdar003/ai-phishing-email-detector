from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load("model/phishing_detector.pkl")

# Simple phishing indicators (rule-based explanation layer)
PHISHING_KEYWORDS = [
    "urgent", "verify", "password", "bank", "suspended",
    "click", "login", "account", "update", "confirm",
    "limited time", "security alert", "immediately"
]

def get_reasons(email_text):
    reasons = []

    text_lower = email_text.lower()

    for word in PHISHING_KEYWORDS:
        if word in text_lower:
            reasons.append(f"Contains suspicious word: '{word}'")

    if "http" in text_lower or "www" in text_lower:
        reasons.append("Contains suspicious link")

    if "!" in email_text:
        reasons.append("Excessive use of exclamation marks")

    if email_text.isupper():
        reasons.append("ALL CAPS text detected (possible scam tone)")

    if len(reasons) == 0:
        reasons.append("No obvious phishing indicators found")

    return reasons


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""
    risk_score = 0
    reasons = []

    if request.method == "POST":
        email = request.form["email"]

        prediction = model.predict([email])[0]
        probabilities = model.predict_proba([email])[0]

        classes = model.classes_
        phishing_index = list(classes).index("phishing")

        risk_score = round(probabilities[phishing_index] * 100, 2)

        reasons = get_reasons(email)

    return render_template(
        "index.html",
        prediction=prediction,
        risk_score=risk_score,
        reasons=reasons
    )


if __name__ == "__main__":
    app.run(debug=True)