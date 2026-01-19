"""
MediSense AI - Flask Backend API
Disease prediction service using trained ML model
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Load trained model and vectorizer
MODEL_PATH = 'model/disease_predictor.pkl'
VECTORIZER_PATH = 'model/symptom_vectorizer.pkl'
DISEASE_INFO_PATH = 'data/disease_info.pkl'

# Global variables for model
model = None
vectorizer = None
disease_info = None

def load_models():
    """Load trained ML models"""
    global model, vectorizer, disease_info
    
    try:
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            print("✓ Disease prediction model loaded")
        else:
            print("⚠ Model not found. Run train_model.py first.")
            
        if os.path.exists(VECTORIZER_PATH):
            vectorizer = joblib.load(VECTORIZER_PATH)
            print("✓ Symptom vectorizer loaded")
            
        if os.path.exists(DISEASE_INFO_PATH):
            disease_info = joblib.load(DISEASE_INFO_PATH)
            print("✓ Disease information loaded")
    except Exception as e:
        print(f"Error loading models: {e}")

# Load models on startup
load_models()

@app.route('/', methods=['GET'])
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'message': 'MediSense AI Backend API',
        'version': '1.0.0',
        'model_loaded': model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict disease based on symptoms
    
    Request Body:
    {
        "symptoms": ["fever", "cough", "headache"]
    }
    
    Response:
    [
        {
            "disease": "Flu",
            "confidence": 85.5,
            "matchedSymptoms": 3,
            "totalSymptoms": 7,
            "recommendations": [...],
            "medications": [...]
        }
    ]
    """
    try:
        # Get symptoms from request
        data = request.get_json()
        
        if not data or 'symptoms' not in data:
            return jsonify({
                'error': 'Missing symptoms in request body'
            }), 400
        
        symptoms = data['symptoms']
        
        if not isinstance(symptoms, list) or len(symptoms) == 0:
            return jsonify({
                'error': 'Symptoms must be a non-empty array'
            }), 400
        
        # Use mock prediction if model not loaded
        if model is None or vectorizer is None:
            return jsonify({
                'error': 'Model not loaded. Using mock predictions.',
                'note': 'Run train_model.py to train the ML model',
                'predictions': mock_predict(symptoms)
            })
        
        # Transform symptoms to feature vector
        symptom_text = ' '.join(symptoms)
        X = vectorizer.transform([symptom_text])
        
        # Get prediction probabilities
        predictions = model.predict_proba(X)[0]
        classes = model.classes_
        
        # Get top 3 predictions
        top_indices = np.argsort(predictions)[-3:][::-1]
        
        results = []
        for idx in top_indices:
            disease = classes[idx]
            confidence = predictions[idx] * 100
            
            if confidence < 5:  # Skip very low confidence predictions
                continue
            
            # Get disease information
            info = disease_info.get(disease.lower(), {
                'recommendations': ['Consult a healthcare professional'],
                'medications': ['See your doctor for proper treatment']
            })
            
            results.append({
                'disease': disease,
                'confidence': min(confidence, 95),  # Cap at 95%
                'matchedSymptoms': len(symptoms),
                'totalSymptoms': len(info.get('symptoms', [])),
                'recommendations': info.get('recommendations', []),
                'medications': info.get('medications', [])
            })
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({
            'error': f'Prediction failed: {str(e)}'
        }), 500

def mock_predict(symptoms):
    """Fallback mock prediction when model is not loaded"""
    return [
        {
            'disease': 'Common Cold',
            'confidence': 75,
            'matchedSymptoms': len(symptoms),
            'totalSymptoms': 6,
            'recommendations': [
                'Get plenty of rest',
                'Stay hydrated',
                'Use over-the-counter cold medications'
            ],
            'medications': [
                'Acetaminophen for fever',
                'Decongestants for congestion'
            ]
        }
    ]

@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    """Get list of all available symptoms"""
    if vectorizer is None:
        return jsonify({
            'error': 'Vectorizer not loaded'
        }), 500
    
    # Get feature names from vectorizer
    symptoms = vectorizer.get_feature_names_out().tolist()
    
    return jsonify({
        'symptoms': symptoms,
        'count': len(symptoms)
    })

@app.route('/diseases', methods=['GET'])
def get_diseases():
    """Get list of all diseases in database"""
    if disease_info is None:
        return jsonify({
            'error': 'Disease information not loaded'
        }), 500
    
    diseases = list(disease_info.keys())
    
    return jsonify({
        'diseases': diseases,
        'count': len(diseases)
    })

@app.route('/disease/<disease_name>', methods=['GET'])
def get_disease_info(disease_name):
    """Get detailed information about a specific disease"""
    if disease_info is None:
        return jsonify({
            'error': 'Disease information not loaded'
        }), 500
    
    info = disease_info.get(disease_name.lower())
    
    if info is None:
        return jsonify({
            'error': f'Disease "{disease_name}" not found'
        }), 404
    
    return jsonify({
        'disease': disease_name.title(),
        'symptoms': info.get('symptoms', []),
        'recommendations': info.get('recommendations', []),
        'medications': info.get('medications', [])
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🏥 MediSense AI Backend Server")
    print("="*50)
    
    if model is None:
        print("\n⚠ WARNING: ML Model not loaded!")
        print("Run: python train_model.py")
        print("Using mock predictions for now.\n")
    
    print("Server starting on http://localhost:5000")
    print("API Endpoints:")
    print("  GET  /              - Health check")
    print("  POST /predict       - Predict disease from symptoms")
    print("  GET  /symptoms      - Get all available symptoms")
    print("  GET  /diseases      - Get all diseases")
    print("  GET  /disease/<name> - Get disease details")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
