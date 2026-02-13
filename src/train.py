import os
import numpy as np
import tensorflow as tf
from data_loader import load_data
from model import build_model
import matplotlib.pyplot as plt

def main():
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'Anemia_Dataset.csv')
    
    print(f"Loading data from {csv_path}...")
    try:
        X_train, X_test, y_train, y_test = load_data(csv_path)
        print(f"Data loaded successfully.")
        print(f"Training shape: {X_train.shape}, {y_train.shape}")
        print(f"Testing shape: {X_test.shape}, {y_test.shape}")
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    # Build model
    input_shape = (X_train.shape[1], 1)
    model = build_model(input_shape)
    model.summary()

    # Train model
    print("Starting training...")
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=8,
        validation_data=(X_test, y_test),
        verbose=1
    )

    # Evaluate model
    print("Evaluating model...")
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f"Test Loss: {loss:.4f}")
    print(f"Test Accuracy: {accuracy:.4f}")

    # Plot training history
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Val Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Val Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig(os.path.join(base_dir, 'training_history.png'))
    print(f"Training history saved to {os.path.join(base_dir, 'training_history.png')}")

    # Save model
    model.save(os.path.join(base_dir, 'anemia_model.h5'))
    print(f"Model saved to {os.path.join(base_dir, 'anemia_model.h5')}")

if __name__ == "__main__":
    main()
