import pandas as pd
import joblib
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load("models/churn_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    data = pd.read_csv(file)
    
    # Example preprocessing
    data['Engagement Score'] = data['Engagement Score'].fillna(0)
    predictions = model.predict_proba(data[['Engagement Score']])[:, 1]  # Probability of churn
    
    data['Churn Probability'] = predictions
    data['Retention Suggestion'] = ["Offer discount" if p > 0.5 else "Maintain engagement" for p in predictions]
    
    return jsonify(data.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
