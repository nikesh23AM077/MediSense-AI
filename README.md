# 🏥 MediSense AI - Disease Prediction System

AI-powered disease prediction system that analyzes symptoms and provides intelligent health insights.

![Project Status](https://img.shields.io/badge/status-demo-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Overview

MediSense AI is a comprehensive disease prediction platform featuring:
- **Interactive Web Interface** - Two input methods (chatbot & symptom checker)
- **Machine Learning Backend** - Random Forest classifier with 87% accuracy
- **24 Disease Coverage** - From common cold to chronic conditions
- **Professional UI/UX** - Modern design with dark mode support

⚠️ **IMPORTANT**: This is a demo/prototype for educational purposes only. Not for actual medical diagnosis.

---

## 🚀 Quick Start

### Option 1: Frontend Demo (No Installation)

1. Open `frontend/index.html` in your browser
2. Try the AI chatbot or symptom checker
3. View instant predictions (uses mock data)

### Option 2: Full Stack with ML Backend

```bash
# 1. Install Python dependencies
cd backend
pip install -r requirements.txt

# 2. Generate training data
python create_dataset.py

# 3. Train the model
python train_model.py

# 4. Start backend server
python app.py
```

Server runs on: `http://localhost:5000`

---

## 📁 Project Structure

```
dis_predition/
├── frontend/               # Web interface
│   ├── pages/             # HTML pages
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── how-it-works.html
│   │   ├── chatbot.html
│   │   ├── symptom-checker.html
│   │   └── results.html
│   ├── css/
│   │   └── styles.css     # Complete design system
│   └── js/
│       ├── script.js      # Core logic
│       ├── chatbot.js     # Chatbot functionality
│       └── symptom-checker.js
│
├── backend/               # Python Flask API
│   ├── app.py            # API server
│   ├── train_model.py    # ML training
│   ├── create_dataset.py # Dataset generator
│   ├── requirements.txt
│   ├── data/             # Training data
│   └── model/            # Trained models
│
└── docs/                 # Documentation
    ├── README.md         # Backend guide
    └── DATA_GUIDE.md     # Data collection
```

---

## 🎯 Features

### Frontend
- ✅ **AI Chatbot** - Natural language symptom input
- ✅ **Symptom Checker** - Structured selection from 60+ symptoms
- ✅ **Results Dashboard** - Confidence scores, recommendations, medications
- ✅ **Dark Mode** - Theme persistence with localStorage
- ✅ **Responsive Design** - Works on all devices

### Backend
- ✅ **RESTful API** - Flask-based prediction service
- ✅ **ML Pipeline** - Random Forest with TF-IDF features
- ✅ **24 Diseases** - Comprehensive medical database
- ✅ **Auto-generated Dataset** - 120+ training samples

---

## 🧠 ML Model Details

| Component | Details |
|-----------|---------|
| **Algorithm** | Random Forest (100 trees) |
| **Features** | TF-IDF vectorization (200 features) |
| **Accuracy** | ~87% (cross-validated) |
| **Training Data** | 120 samples, 24 diseases |
| **Symptoms** | 200+ unique symptoms |

---

## 📡 API Endpoints

```http
GET  /                    # Health check
POST /predict             # Predict disease
GET  /symptoms            # List all symptoms
GET  /diseases            # List all diseases
GET  /disease/<name>      # Get disease details
```

**Example Request:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"symptoms": ["fever", "cough", "headache"]}'
```

---

## 🎨 Technologies

**Frontend:**
- HTML5, CSS3, JavaScript (ES6)
- Responsive design with CSS Grid/Flexbox
- LocalStorage for persistence

**Backend:**
- Python 3.8+
- Flask (web framework)
- scikit-learn (machine learning)
- pandas, numpy (data processing)

**ML Pipeline:**
- TF-IDF Vectorizer
- Random Forest Classifier
- 5-fold cross-validation

---

## 📚 Documentation

- **[Backend Setup Guide](docs/README.md)** - API documentation & setup
- **[Data Collection Guide](docs/DATA_GUIDE.md)** - How to gather medical data
- **[Walkthrough](docs/WALKTHROUGH.md)** - Complete project walkthrough

---

## 🔮 24 Diseases Covered

| Category | Diseases |
|----------|----------|
| **Respiratory** | Common Cold, Flu, Pneumonia, Bronchitis, Asthma |
| **Gastrointestinal** | Gastroenteritis, Food Poisoning, Acid Reflux, IBS |
| **Neurological** | Migraine, Tension Headache |
| **Cardiovascular** | Hypertension, Angina |
| **Metabolic** | Diabetes, Hypoglycemia |
| **Mental Health** | Anxiety, Depression |
| **Infections** | UTI, Strep Throat |
| **Musculoskeletal** | Arthritis, Fibromyalgia |
| **Skin** | Eczema, Psoriasis |

---

## 🛠️ Development

### Adding More Diseases

Edit `backend/create_dataset.py`:

```python
disease_data['New Disease'] = [
    'symptom1', 'symptom2', 'symptom3'
]
```

Then retrain:
```bash
python create_dataset.py
python train_model.py
```

### Integrating Real Model

Update `frontend/js/script.js`:

```javascript
async function predictDisease(symptoms) {
  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ symptoms })
  });
  return await response.json();
}
```

---

## ⚠️ Disclaimer

**FOR EDUCATIONAL/DEMO PURPOSES ONLY**

This system:
- ❌ Is NOT a substitute for professional medical advice
- ❌ Should NOT be used for actual diagnosis
- ❌ Cannot replace doctor consultations
- ❌ Does not handle medical emergencies

**Always consult qualified healthcare providers for medical concerns.**

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

This is a demo project. For production use:
1. Collect real medical data (ethically sourced)
2. Train with larger datasets
3. Validate with medical professionals
4. Implement proper security measures
5. Add comprehensive legal disclaimers

---

## 📞 Support

For issues or questions:
- Check documentation in `docs/` folder
- Review code comments
- Test with the demo data first

---

**Built with ❤️ for educational purposes**

*Remember: Real healthcare decisions require real doctors!* 🏥
