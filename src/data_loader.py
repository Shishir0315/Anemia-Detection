import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(csv_path):
    """
    Loads and preprocesses the Anemia dataset.
    """
    df = pd.read_csv(csv_path)
    
    # Strip whitespace from column names
    df.columns = df.columns.str.strip()
    
    # Feature selection
    # Inputs: Sex, %Red Pixel, %Green pixel, %Blue pixel
    # Target: Anaemic
    
    # Encode Sex: M -> 1, F -> 0 (or label encoder)
    le_sex = LabelEncoder()
    df['Sex'] = le_sex.fit_transform(df['Sex'])
    
    # Encode Target: Yes -> 1, No -> 0
    le_target = LabelEncoder()
    df['Anaemic'] = le_target.fit_transform(df['Anaemic'])
    
    X = df[['Sex', '%Red Pixel', '%Green pixel', '%Blue pixel']].values
    y = df['Anaemic'].values
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Reshape for Conv1D: (samples, features, 1)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
    
    return X_train, X_test, y_train, y_test
