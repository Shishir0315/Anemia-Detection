import os
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder
from data_loader import load_data

def predict_single(sex, red, green, blue):
    """
    Predicts Anemia status for a single input.
    """
    # 1. Load dataset to refit Scaler (simulating production pipeline)
    # Ideally, we would save the scaler with joblib during training.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'Anemia_Dataset.csv')
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    
    # Fit Scaler on numeric columns
    scaler = StandardScaler()
    numeric_cols = ['%Red Pixel', '%Green pixel', '%Blue pixel']
    scaler.fit(df[numeric_cols])
    
    # 2. Process Input
    # Sex: M -> 1, F -> 0 (based on training logic: M came after F alphabetically? No, LabelEncoder does F=0, M=1)
    # Let's verify LabelEncoder behavior: 'F' < 'M', so F=0, M=1.
    sex_encoded = 1 if sex.upper() == 'M' else 0
    
    # Scale numeric features
    features = np.array([[red, green, blue]])
    features_scaled = scaler.transform(features)
    
    # Combine: [Sex, Red, Green, Blue]
    # Note: In data_loader.py, order is ['Sex', '%Red Pixel', '%Green pixel', '%Blue pixel']
    # And Sex was label encoded (0 or 1). Specific scaling wasn't applied to Sex column usually, 
    # but let's check data_loader.py... 
    # "scaler.fit_transform(X_train)" scalles ALL columns including Sex if passed together.
    # In data_loader.py: X = df[['Sex', ...]].values. Scaler fits on X. 
    # So Sex IS scaled. We need to fit scaler on ALL 4 columns.
    
    # RE-DO SCALER FIT
    le_sex = LabelEncoder()
    df['Sex'] = le_sex.fit_transform(df['Sex']) # F=0, M=1
    
    X_all = df[['Sex', '%Red Pixel', '%Green pixel', '%Blue pixel']].values
    scaler_all = StandardScaler()
    scaler_all.fit(X_all)
    
    # Transform input
    input_vector = np.array([[sex_encoded, red, green, blue]])
    input_scaled = scaler_all.transform(input_vector)
    
    # Reshape for CNN: (1, 4, 1)
    input_reshaped = input_scaled.reshape((1, 4, 1))
    
    # 3. Load Model
    model_path = os.path.join(base_dir, 'anemia_model.h5')
    model = tf.keras.models.load_model(model_path)
    
    # 4. Predict
    prediction = model.predict(input_reshaped)
    probability = prediction[0][0]
    
    result = "Anaemic" if probability > 0.5 else "Not Anaemic"
    return result, probability

if __name__ == "__main__":
    print("--- Anemia Prediction Tool ---")
    print("Enter patient details:")
    sex = input("Sex (M/F): ")
    red = float(input("% Red Pixel: "))
    green = float(input("% Green Pixel: "))
    blue = float(input("% Blue Pixel: "))
    
    try:
        result, prob = predict_single(sex, red, green, blue)
        print(f"\nPrediction: {result}")
        print(f"Confidence (Probability of Anemia): {prob:.2%}")
    except Exception as e:
        print(f"Error: {e}")
