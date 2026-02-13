import os
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from data_loader import load_data
import matplotlib.pyplot as plt

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'Anemia_Dataset.csv')
    
    print(f"Loading data from {csv_path}...")
    try:
        X_train, X_test, y_train, y_test = load_data(csv_path)
        # Reshape back to 2D for Random Forest (samples, features)
        X_train = X_train.reshape(X_train.shape[0], -1)
        X_test = X_test.reshape(X_test.shape[0], -1)
        
        print(f"Data loaded successfully.")
        print(f"Training shape: {X_train.shape}, {y_train.shape}")
        print(f"Testing shape: {X_test.shape}, {y_test.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Build Random Forest model
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Test Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Save results
    with open(os.path.join(base_dir, 'ml_results.txt'), 'w') as f:
        f.write(f"Test Accuracy: {accuracy:.4f}\n")
        f.write("\nClassification Report:\n")
        f.write(classification_report(y_test, y_pred))
    
    print(f"Results saved to {os.path.join(base_dir, 'ml_results.txt')}")

if __name__ == "__main__":
    main()
