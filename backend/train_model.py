"""
MediSense AI - ML Model Training Script
Train a disease prediction model using symptom data
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

def load_data():
    """Load training data"""
    print("Loading training data...")
    
    data_path = 'data/training_data.csv'
    
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found!")
        print("Run: python create_dataset.py first")
        return None
    
    df = pd.read_csv(data_path)
    print(f"✓ Loaded {len(df)} training samples")
    print(f"✓ Found {df['disease'].nunique()} unique diseases")
    
    return df

def prepare_features(df):
    """Convert symptoms text to feature vectors"""
    print("\nPreparing features...")
    
    # Use TF-IDF vectorizer to convert symptoms to numerical features
    vectorizer = TfidfVectorizer(
        max_features=200,  # Limit to top 200 features
        ngram_range=(1, 2),  # Use unigrams and bigrams
        lowercase=True,
        min_df=2  # Ignore terms that appear in fewer than 2 documents
    )
    
    X = vectorizer.fit_transform(df['symptoms'])
    y = df['disease']
    
    print(f"✓ Created feature matrix: {X.shape}")
    print(f"✓ Number of features: {len(vectorizer.get_feature_names_out())}")
    
    return X, y, vectorizer

def train_model(X, y):
    """Train Random Forest classifier"""
    print("\nTraining model...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"✓ Training set: {X_train.shape[0]} samples")
    print(f"✓ Test set: {X_test.shape[0]} samples")
    
    # Train Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate
    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)
    
    print(f"\n✓ Training accuracy: {train_accuracy:.2%}")
    print(f"✓ Test accuracy: {test_accuracy:.2%}")
    
    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5)
    print(f"✓ Cross-validation accuracy: {cv_scores.mean():.2%} (+/- {cv_scores.std():.2%})")
    
    # Detailed evaluation
    y_pred = model.predict(X_test)
    
    print("\n" + "="*60)
    print("Classification Report:")
    print("="*60)
    print(classification_report(y_test, y_pred))
    
    return model, X_test, y_test

def save_model(model, vectorizer):
    """Save trained model and vectorizer"""
    print("\nSaving model...")
    
    # Create model directory
    os.makedirs('model', exist_ok=True)
    
    # Save model
    joblib.dump(model, 'model/disease_predictor.pkl')
    print("✓ Saved model to model/disease_predictor.pkl")
    
    # Save vectorizer
    joblib.dump(vectorizer, 'model/symptom_vectorizer.pkl')
    print("✓ Saved vectorizer to model/symptom_vectorizer.pkl")
    
    # Copy disease info to model folder
    import shutil
    if os.path.exists('data/disease_info.pkl'):
        shutil.copy('data/disease_info.pkl', 'model/disease_info.pkl')
        print("✓ Saved disease info to model/disease_info.pkl")

def test_prediction(model, vectorizer):
    """Test the model with example symptoms"""
    print("\n" + "="*60)
    print("Testing Predictions:")
    print("="*60)
    
    test_cases = [
        {
            'symptoms': ['fever', 'cough', 'sore throat', 'fatigue'],
            'expected': 'Flu or Common Cold'
        },
        {
            'symptoms': ['severe headache', 'nausea', 'sensitivity to light'],
            'expected': 'Migraine'
        },
        {
            'symptoms': ['frequent urination', 'excessive thirst', 'fatigue'],
            'expected': 'Diabetes'
        },
        {
            'symptoms': ['chest pain', 'shortness of breath', 'cough'],
            'expected': 'Pneumonia or Bronchitis'
        },
        {
            'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal pain'],
            'expected': 'Gastroenteritis'
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        symptoms = test_case['symptoms']
        expected = test_case['expected']
        
        # Convert to text
        symptom_text = ' '.join(symptoms)
        X = vectorizer.transform([symptom_text])
        
        # Predict
        prediction = model.predict(X)[0]
        probabilities = model.predict_proba(X)[0]
        confidence = max(probabilities) * 100
        
        # Get top 3 predictions
        top_3_idx = np.argsort(probabilities)[-3:][::-1]
        top_3 = [(model.classes_[idx], probabilities[idx] * 100) for idx in top_3_idx]
        
        print(f"\nTest Case {i}:")
        print(f"  Symptoms: {', '.join(symptoms)}")
        print(f"  Expected: {expected}")
        print(f"  Predicted: {prediction} ({confidence:.1f}% confidence)")
        print(f"  Top 3 predictions:")
        for disease, prob in top_3:
            print(f"    - {disease}: {prob:.1f}%")

def main():
    """Main training pipeline"""
    print("\n" + "="*60)
    print("🤖 MediSense AI - Model Training Pipeline")
    print("="*60 + "\n")
    
    # Step 1: Load data
    df = load_data()
    if df is None:
        return
    
    # Step 2: Prepare features
    X, y, vectorizer = prepare_features(df)
    
    # Step 3: Train model
    model, X_test, y_test = train_model(X, y)
    
    # Step 4: Save model
    save_model(model, vectorizer)
    
    # Step 5: Test predictions
    test_prediction(model, vectorizer)
    
    print("\n" + "="*60)
    print("✓ Training Complete!")
    print("="*60)
    print("\nNext steps:")
    print("  1. Run: python app.py")
    print("  2. The backend will load the trained model")
    print("  3. Update frontend to use API: http://localhost:5000/predict")
    print("\n")

if __name__ == '__main__':
    main()
