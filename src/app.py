from flask import Flask, request, jsonify
import pandas as pd
import joblib
from src.features.build_features import build_features
from src.utils.helpers import preprocess_data

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model/linear_regression.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df = pd.DataFrame(data)
    df = preprocess_data(df)
    df = build_features(df)
    
    predictions = model.predict(df)
    return jsonify(predictions.tolist())


if __name__ == '__main__':
    app.run(debug=True)
