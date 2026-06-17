
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sentence_transformers import SentenceTransformer

# Load SentenceTransformer model for semantic embeddings
model_sbert = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    return model_sbert.encode(text)

def load_and_preprocess_data(filepath="error_data.csv"):
    df = pd.read_csv(filepath)
    
    # Generate semantic embeddings for error messages
    df["error_embedding"] = df["error_message"].apply(generate_embedding)
    
    # Features (X) and Target (y)
    X = np.array(df["error_embedding"].tolist())
    y = df["human_explanation"].values
    
    # Encode target variable
    label_encoder_explanation = LabelEncoder()
    y_encoded = label_encoder_explanation.fit_transform(y)
    
    return X, y_encoded, label_encoder_explanation

# Placeholder for model training
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    print("DebugMind: AI for Explaining Code Errors in Human Language")
    print("----------------------------------------------------------")
    print("1. Simulating data...")
    try:
        from data_simulator import simulate_error_data
        simulate_error_data(num_samples=2000).to_csv("error_data.csv", index=False)
        print("Simulated data generated: error_data.csv")
    except Exception as e:
        print(f"Could not simulate data: {e}. Attempting to load existing data.")

    print("2. Loading and preprocessing data (generating embeddings)...")
    X, y_encoded, label_encoder_explanation = load_and_preprocess_data()
    print(f"Data loaded. X shape: {X.shape}, y shape: {y_encoded.shape}")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    print(f"Data split. Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    print("3. Training model...")
    model = train_model(X_train, y_train)

    print("4. Evaluating model...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {accuracy*100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=label_encoder_explanation.classes_))

    print("5. Making a sample prediction...")
    sample_error_message = "TypeError: unsupported operand type(s) for +: 'int' and 'str'"
    sample_error_embedding = generate_embedding(sample_error_message)
    sample_error_embedding_reshaped = sample_error_embedding.reshape(1, -1)
    
    prediction = model.predict(sample_error_embedding_reshaped)
    predicted_explanation = label_encoder_explanation.inverse_transform(prediction)[0]
    
    print(f"\nSample Error Message: \"{sample_error_message}\"")
    print(f"Predicted Human Explanation: {predicted_explanation}")

    print("DebugMind project setup complete. Further development is required for a more sophisticated explanation model and real-world integration.")
