import os
import numpy as np
import pandas as pd
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Global variables for model and scaler
model = None
scaler = None

def load_resources():
    global model, scaler
    try:
        # Load Model
        print("Loading Model...")
        model_path = os.path.join(os.path.dirname(__file__), 'anemia_model.h5')
        if not os.path.exists(model_path):
             # Fallback if executing from src/ folder context vs root
             model_path = 'anemia_model.h5'
        
        model = tf.keras.models.load_model(model_path)
        print("Model Loaded Successfully.")

        # Fit Scaler (Simulating production pipeline by refitting on training data)
        print("Initializing Preprocessing...")
        csv_path = 'Anemia_Dataset.csv'
        if not os.path.exists(csv_path):
            csv_path = '../Anemia_Dataset.csv' # Try prompt up dir if needed
            
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            df.columns = df.columns.str.strip()
            
            # Encode Sex for fitting
            le_sex = LabelEncoder()
            df['Sex'] = le_sex.fit_transform(df['Sex']) # F->0, M->1
            
            # Fit scaler on all features: Sex, R, G, B
            X_all = df[['Sex', '%Red Pixel', '%Green pixel', '%Blue pixel']].values
            scaler = StandardScaler()
            scaler.fit(X_all)
            print("Scaler Fitted Successfully.")
        else:
            print("Warning: CSV not found for scaler fitting. Predictions may be inaccurate.")
            
    except Exception as e:
        print(f"Error initializing resources: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from JSON request
        data = request.json
        sex = data.get('sex', '').upper()
        red = float(data.get('red'))
        green = float(data.get('green'))
        blue = float(data.get('blue'))

        # Preprocess
        # Sex: M -> 1, F -> 0
        sex_val = 1 if sex == 'M' else 0
        
        # Create feature vector
        features = np.array([[sex_val, red, green, blue]])
        
        # Scale
        if scaler:
            features_scaled = scaler.transform(features)
        else:
            features_scaled = features # Fallback (shouldn't happen)
            
        # Reshape for CNN: (1, 4, 1)
        # Note: If model was trained with (batch, 4, 1), input must match dimensionality
        input_data = features_scaled.reshape((1, 4, 1))
        
        # Predict
        prediction = model.predict(input_data)
        probability = float(prediction[0][0])
        
        label = "Anemic" if probability > 0.5 else "Non-Anemic"
        confidence = probability if probability > 0.5 else 1 - probability
        
        return jsonify({
            'label': label,
            'confidence': f"{confidence:.2%}",
            'raw_prob': probability
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    load_resources()
    app.run(debug=True, port=5000)
