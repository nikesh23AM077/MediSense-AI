# MediSense AI - Data Collection & Preparation Guide

## 📊 Understanding Medical Datasets

For building a robust disease prediction model, you need quality symptom-disease data. Here's how to collect and prepare it.

---

## 1. Data Sources

### Free Public Datasets

#### **Kaggle**
- **Disease Symptom Dataset**: https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset
- **Symptom-Disease Diagnosis**: https://www.kaggle.com/datasets/kaushil268/disease-prediction-using-machine-learning
- **Medical Dataset**: Various structured medical datasets

#### **UCI Machine Learning Repository**
- Medical diagnosis datasets
- Clinical data collections
- https://archive.ics.uci.edu/ml/datasets.php?format=&task=cla&att=&area=&numAtt=&numIns=&type=&sort=nameUp&view=table

#### **Research Papers**
- PubMed Central (open access papers with datasets)
- Medical research institutions
- Academic databases

### Medical Knowledge Bases

- **MedlinePlus**: https://medlineplus.gov/
- **Mayo Clinic**: Symptom checkers and disease info
- **WebMD Symptom Checker**: Disease-symptom relationships
- **CDC**: Disease information

---

## 2. Data Format

### Recommended Structure

**CSV Format:**
```csv
disease,symptom1,symptom2,symptom3,...,severity,duration
Flu,1,1,0,...,moderate,3-7 days
Common Cold,0,1,1,...,mild,7-10 days
```

**Or text-based:**
```csv
disease,symptoms
Flu,"fever cough sore throat body aches"
Common Cold,"runny nose sneezing sore throat"
```

### Required Fields

1. **Disease Name** (target variable)
2. **Symptoms** (features)
3. **Optional**: severity, duration, demographics

---

## 3. Manual Data Collection

If collecting your own data:

### Step 1: Define Disease Categories

```python
diseases = [
    'Common Cold', 'Flu', 'Pneumonia',
    'Allergies', 'Asthma', 'Bronchitis',
    # ... add more
]
```

### Step 2: List Symptoms for Each Disease

Create a spreadsheet or JSON file:

```json
{
  "Common Cold": {
    "common_symptoms": ["runny nose", "sore throat", "cough"],
    "occasional_symptoms": ["headache", "fatigue"],
    "rare_symptoms": ["fever"],
    "severity": "mild",
    "duration": "7-10 days"
  }
}
```

### Step 3: Generate Training Samples

The `create_dataset.py` script does this automatically by:
1. Taking disease-symptom mappings
2. Creating multiple samples per disease
3. Randomly selecting symptoms (3-7 per sample)
4. Generating realistic combinations

---

## 4. Data Cleaning

### Remove Duplicates

```python
df = df.drop_duplicates()
```

### Standardize Symptom Names

```python
symptom_mapping = {
    'headache': ['head pain', 'head ache', 'cephalgia'],
    'fever': ['high temperature', 'pyrexia'],
    'nausea': ['feeling sick', 'queasiness']
}

def standardize_symptom(symptom):
    for standard, variants in symptom_mapping.items():
        if symptom.lower() in variants:
            return standard
    return symptom.lower()
```

### Handle Missing Values

```python
# Drop rows with missing disease labels
df = df.dropna(subset=['disease'])

# Fill missing symptoms with 'none'
df['symptoms'] = df['symptoms'].fillna('none')
```

---

## 5. Data Augmentation

### Expand Dataset Size

```python
def augment_data(df, multiplier=3):
    """Create variations of existing samples"""
    augmented = []
    
    for _, row in df.iterrows():
        disease = row['disease']
        symptoms = row['symptoms'].split()
        
        # Create variations
        for i in range(multiplier):
            # Randomly drop 1-2 symptoms
            subset = random.sample(symptoms, 
                                 len(symptoms) - random.randint(1, 2))
            
            augmented.append({
                'disease': disease,
                'symptoms': ' '.join(subset)
            })
    
    return pd.DataFrame(augmented)
```

### Add Synonyms

```python
synonyms = {
    'headache': ['head pain', 'cephalgia'],
    'fever': ['high temp', 'pyrexia'],
}

def add_synonyms(text):
    words = text.split()
    for i, word in enumerate(words):
        if word in synonyms:
            words[i] = random.choice([word] + synonyms[word])
    return ' '.join(words)
```

---

## 6. Feature Engineering

### Binary Encoding

Convert symptoms to 0/1 matrix:

```python
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
symptom_matrix = mlb.fit_transform(symptoms_lists)
```

### TF-IDF (Current Approach)

Better for text-based symptoms:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=200)
X = vectorizer.fit_transform(symptom_texts)
```

### Custom Features

```python
# Add symptom count
df['symptom_count'] = df['symptoms'].str.split().str.len()

# Add severity scores
severity_map = {'mild': 1, 'moderate': 2, 'severe': 3}
df['severity_score'] = df['severity'].map(severity_map)
```

---

## 7. Validation Strategy

### Split Data Properly

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,
    stratify=y,  # Maintain class balance
    random_state=42
)
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(f"CV Accuracy: {scores.mean():.2%} (+/- {scores.std():.2%})")
```

---

## 8. Data Quality Checklist

✅ **Completeness**
- All diseases have sufficient samples (5+ each)
- All symptoms are properly labeled
- No missing critical information

✅ **Consistency**
- Symptom names standardized
- Disease names uniform
- Same format throughout

✅ **Balance**
- Similar sample counts per disease
- Not too skewed toward common diseases

✅ **Accuracy**
- Medical facts verified
- Symptoms match actual diseases
- No contradictory information

✅ **Diversity**
- Various symptom combinations
- Different severity levels
- Range of diseases covered

---

## 9. Expanding the Current Dataset

### Add More Diseases

Edit `create_dataset.py`:

```python
disease_data = {
    # Add new disease
    'Malaria': [
        'high fever', 'chills', 'sweating',
        'headache', 'nausea', 'vomiting',
        'muscle pain', 'fatigue'
    ],
    
    # Add more...
}
```

### Add More Symptoms

```python
disease_data['Flu'] = [
    'fever', 'chills', 'cough',
    'sore throat', 'body aches',
    'headache', 'fatigue',
    'loss of appetite',  # New
    'muscle weakness'    # New
]
```

---

## 10. Real-World Data Collection

### From Medical Records (If Available)

**Requirements:**
- HIPAA compliance
- Patient consent
- De-identification
- IRB approval

**Format:**
```python
{
    'patient_id': 'XXXX',  # Anonymized
    'symptoms': [...],
    'diagnosis': 'Disease Name',
    'age_group': '30-40',
    'severity': 'moderate'
}
```

### From Surveys

Create a symptom reporting form:
- Online questionnaire
- Collect symptoms experienced
- Verified diagnosis (if known)
- Demographic info (optional)

---

## 11. Dataset Quality Metrics

### Check Class Distribution

```python
print(df['disease'].value_counts())

# Should be relatively balanced
# Each disease: 5-10% of total samples
```

### Check Symptom Coverage

```python
all_symptoms = set()
for symptoms in df['symptoms']:
    all_symptoms.update(symptoms.split())

print(f"Total unique symptoms: {len(all_symptoms)}")
# Target: 50-200 symptoms
```

### Validate Correlations

```python
# Symptoms should correlate with specific diseases
from sklearn.feature_selection import chi2

chi2_scores, p_values = chi2(X, y)
top_features = np.argsort(chi2_scores)[-20:]
print("Most predictive symptoms:", 
      vectorizer.get_feature_names()[top_features])
```

---

## 12. Example: Building Custom Dataset

```python
import pandas as pd
import json

# Step 1: Define diseases and symptoms
data = {
    'Flu': {
        'symptoms': ['fever', 'cough', 'fatigue', 'body aches'],
        'samples': 10
    },
    'Cold': {
        'symptoms': ['runny nose', 'sneezing', 'sore throat'],
        'samples': 10
    }
}

# Step 2: Generate samples
rows = []
for disease, info in data.items():
    for i in range(info['samples']):
        # Select 2-4 random symptoms
        n = random.randint(2, 4)
        symptoms = random.sample(info['symptoms'], n)
        
        rows.append({
            'disease': disease,
            'symptoms': ' '.join(symptoms)
        })

# Step 3: Create DataFrame and save
df = pd.DataFrame(rows)
df.to_csv('custom_dataset.csv', index=False)
```

---

## Summary

**For best results:**

1. Start with `create_dataset.py` (24 diseases included)
2. Add more diseases as needed
3. Collect real data if possible
4. Clean and validate thoroughly
5. Use augmentation to expand
6. Retrain model regularly with new data

The quality of your model depends directly on the quality of your data! 📊
