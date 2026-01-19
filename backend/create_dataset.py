"""
MediSense AI - Sample Training Dataset
Contains disease-symptom mappings for training the ML model
"""

import pandas as pd
import joblib

# Expanded disease database with 20+ diseases
disease_data = {
    # Disease: [symptoms list]
    
    # Respiratory Infections
    'Common Cold': ['runny nose', 'sore throat', 'cough', 'sneezing', 'congestion', 'headache', 'fatigue', 'mild fever'],
    
    'Flu': ['high fever', 'chills', 'muscle aches', 'fatigue', 'cough', 'sore throat', 'headache', 'body aches', 'weakness'],
    
    'Pneumonia': ['high fever', 'cough', 'chest pain', 'shortness of breath', 'fatigue', 'sweating', 'chills', 'rapid breathing'],
    
    'Bronchitis': ['cough', 'mucus production', 'chest discomfort', 'fatigue', 'shortness of breath', 'mild fever', 'wheezing'],
    
    # Allergies & Immune
    'Allergies': ['sneezing', 'runny nose', 'itchy eyes', 'watery eyes', 'congestion', 'skin rash', 'itching', 'scratchy throat'],
    
    'Asthma': ['shortness of breath', 'wheezing', 'chest tightness', 'cough', 'difficulty breathing', 'rapid breathing'],
    
    # Gastrointestinal
    'Gastroenteritis': ['nausea', 'vomiting', 'diarrhea', 'abdominal pain', 'stomach cramps', 'fever', 'dehydration', 'loss of appetite'],
    
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'abdominal cramps', 'fever', 'weakness', 'headache', 'dehydration'],
    
    'Acid Reflux': ['heartburn', 'chest pain', 'difficulty swallowing', 'regurgitation', 'sour taste', 'cough', 'sore throat'],
    
    'Irritable Bowel Syndrome': ['abdominal pain', 'bloating', 'gas', 'diarrhea', 'constipation', 'cramping', 'mucus in stool'],
    
    # Neurological
    'Migraine': ['severe headache', 'nausea', 'vomiting', 'sensitivity to light', 'sensitivity to sound', 'visual disturbances', 'dizziness', 'throbbing pain'],
    
    'Tension Headache': ['headache', 'tightness around head', 'pressure in forehead', 'neck pain', 'shoulder pain', 'mild sensitivity to light'],
    
    # Cardiovascular
    'Hypertension': ['headache', 'dizziness', 'blurred vision', 'chest pain', 'shortness of breath', 'fatigue', 'irregular heartbeat', 'nosebleeds'],
    
    'Angina': ['chest pain', 'chest pressure', 'shortness of breath', 'pain in arms', 'pain in neck', 'sweating', 'nausea', 'fatigue'],
    
    # Metabolic
    'Diabetes': ['frequent urination', 'excessive thirst', 'extreme hunger', 'fatigue', 'blurred vision', 'slow healing', 'tingling in hands', 'tingling in feet', 'weight loss'],
    
    'Hypoglycemia': ['shakiness', 'sweating', 'rapid heartbeat', 'dizziness', 'hunger', 'irritability', 'confusion', 'pale skin'],
    
    # Mental Health
    'Anxiety': ['excessive worry', 'restlessness', 'rapid heartbeat', 'sweating', 'trembling', 'difficulty concentrating', 'sleep problems', 'fatigue', 'irritability'],
    
    'Depression': ['persistent sadness', 'loss of interest', 'fatigue', 'sleep problems', 'appetite changes', 'difficulty concentrating', 'feelings of worthlessness', 'hopelessness'],
    
    # Infections
    'Urinary Tract Infection': ['frequent urination', 'painful urination', 'burning sensation', 'cloudy urine', 'strong urine odor', 'pelvic pain', 'lower back pain', 'fever'],
    
    'Strep Throat': ['severe sore throat', 'painful swallowing', 'fever', 'red tonsils', 'white patches', 'swollen lymph nodes', 'headache', 'rash'],
    
    # Musculoskeletal
    'Arthritis': ['joint pain', 'joint stiffness', 'swelling', 'reduced range of motion', 'redness', 'warmth in joints', 'fatigue'],
    
    'Fibromyalgia': ['widespread pain', 'fatigue', 'sleep problems', 'cognitive difficulties', 'headaches', 'mood issues', 'numbness', 'tingling'],
    
    # Skin Conditions
    'Eczema': ['itchy skin', 'red patches', 'dry skin', 'thickened skin', 'small bumps', 'oozing', 'crusting'],
    
    'Psoriasis': ['red patches', 'silvery scales', 'dry skin', 'itching', 'burning', 'thick skin', 'joint pain'],
}

# Disease information (recommendations and medications)
disease_info = {
    'common cold': {
        'symptoms': disease_data['Common Cold'],
        'recommendations': [
            'Get plenty of rest and sleep',
            'Stay hydrated by drinking lots of fluids',
            'Use a humidifier to ease congestion',
            'Gargle with salt water for sore throat',
            'Avoid smoking and secondhand smoke'
        ],
        'medications': [
            'Acetaminophen (Tylenol) for fever and pain',
            'Decongestants (Pseudoephedrine) for congestion',
            'Cough suppressants (Dextromethorphan)',
            'Vitamin C and Zinc supplements'
        ]
    },
    'flu': {
        'symptoms': disease_data['Flu'],
        'recommendations': [
            'Rest and avoid physical exertion',
            'Stay home to prevent spreading',
            'Drink plenty of fluids',
            'Monitor fever and seek help if very high',
            'Use cool compresses for fever'
        ],
        'medications': [
            'Antiviral medications (Tamiflu, Relenza)',
            'Acetaminophen or Ibuprofen for fever',
            'Decongestants for congestion',
            'Cough medicine (Dextromethorphan)'
        ]
    },
    'pneumonia': {
        'symptoms': disease_data['Pneumonia'],
        'recommendations': [
            'Seek immediate medical attention',
            'Complete full course of antibiotics',
            'Rest and conserve energy',
            'Stay hydrated',
            'Use humidifier for breathing comfort'
        ],
        'medications': [
            'Antibiotics (prescribed by doctor)',
            'Fever reducers (Acetaminophen)',
            'Cough medicine if prescribed',
            'Pain relievers for chest pain'
        ]
    },
    'bronchitis': {
        'symptoms': disease_data['Bronchitis'],
        'recommendations': [
            'Get plenty of rest',
            'Drink warm fluids',
            'Use humidifier',
            'Avoid irritants like smoke',
            'Practice breathing exercises'
        ],
        'medications': [
            'Cough suppressants',
            'Bronchodilators if wheezing',
            'Antibiotics only if bacterial',
            'Pain relievers for discomfort'
        ]
    },
    'allergies': {
        'symptoms': disease_data['Allergies'],
        'recommendations': [
            'Identify and avoid allergen triggers',
            'Keep windows closed during high pollen',
            'Use air purifiers indoors',
            'Shower after outdoor activities',
            'Wash bedding regularly in hot water'
        ],
        'medications': [
            'Antihistamines (Cetirizine, Loratadine)',
            'Nasal corticosteroid sprays (Flonase)',
            'Decongestants for congestion',
            'Eye drops for itchy eyes'
        ]
    },
    'asthma': {
        'symptoms': disease_data['Asthma'],
        'recommendations': [
            'Use inhaler as prescribed',
            'Avoid triggers (smoke, allergens)',
            'Monitor peak flow regularly',
            'Have action plan for attacks',
            'Exercise with doctor guidance'
        ],
        'medications': [
            'Rescue inhaler (Albuterol)',
            'Controller medications (Inhaled corticosteroids)',
            'Long-acting bronchodilators',
            'Leukotriene modifiers'
        ]
    },
    'gastroenteritis': {
        'symptoms': disease_data['Gastroenteritis'],
        'recommendations': [
            'Stay hydrated with electrolyte solutions',
            'Follow BRAT diet (Bananas, Rice, Applesauce, Toast)',
            'Rest and avoid solid foods initially',
            'Practice good hand hygiene',
            'Avoid dairy temporarily'
        ],
        'medications': [
            'Oral rehydration solutions (Pedialyte)',
            'Anti-nausea medications (Ondansetron)',
            'Probiotics for gut health',
            'Avoid anti-diarrheal unless prescribed'
        ]
    },
    'food poisoning': {
        'symptoms': disease_data['Food Poisoning'],
        'recommendations': [
            'Stay hydrated',
            'Rest and let body recover',
            'Avoid solid foods until nausea subsides',
            'Practice food safety in future',
            'Seek medical help if severe'
        ],
        'medications': [
            'Oral rehydration solutions',
            'Anti-nausea medication if prescribed',
            'Electrolyte replacement',
            'Antibiotics only if bacterial (prescribed)'
        ]
    },
    'acid reflux': {
        'symptoms': disease_data['Acid Reflux'],
        'recommendations': [
            'Avoid trigger foods (spicy, acidic)',
            'Eat smaller, frequent meals',
            'Avoid lying down after eating',
            'Elevate head while sleeping',
            'Maintain healthy weight'
        ],
        'medications': [
            'Antacids (Tums, Rolaids)',
            'H2 blockers (Famotidine)',
            'Proton pump inhibitors (Omeprazole)',
            'Alginates for coating'
        ]
    },
    'irritable bowel syndrome': {
        'symptoms': disease_data['Irritable Bowel Syndrome'],
        'recommendations': [
            'Follow low-FODMAP diet',
            'Manage stress levels',
            'Exercise regularly',
            'Keep food diary',
            'Eat regular meals'
        ],
        'medications': [
            'Antispasmodics for cramping',
            'Fiber supplements',
            'Anti-diarrheal medications',
            'Laxatives if constipated'
        ]
    },
    'migraine': {
        'symptoms': disease_data['Migraine'],
        'recommendations': [
            'Rest in quiet, dark room',
            'Apply cold compress to forehead',
            'Avoid triggers (bright lights, loud sounds)',
            'Practice relaxation techniques',
            'Maintain regular sleep schedule'
        ],
        'medications': [
            'Triptans (Sumatriptan, Rizatriptan)',
            'NSAIDs (Ibuprofen, Naproxen)',
            'Anti-nausea medications',
            'Preventive medications if frequent'
        ]
    },
    'tension headache': {
        'symptoms': disease_data['Tension Headache'],
        'recommendations': [
            'Rest and relax',
            'Apply heat or cold to affected area',
            'Massage neck and shoulders',
            'Practice stress management',
            'Maintain good posture'
        ],
        'medications': [
            'Acetaminophen (Tylenol)',
            'Ibuprofen (Advil)',
            'Combination pain relievers',
            'Muscle relaxants if needed'
        ]
    },
    'hypertension': {
        'symptoms': disease_data['Hypertension'],
        'recommendations': [
            'Reduce sodium intake',
            'Exercise regularly (30 min daily)',
            'Maintain healthy weight',
            'Limit alcohol consumption',
            'Quit smoking',
            'Monitor blood pressure regularly'
        ],
        'medications': [
            'ACE inhibitors (Lisinopril)',
            'Beta-blockers (Metoprolol)',
            'Calcium channel blockers',
            'Diuretics (water pills)'
        ]
    },
    'angina': {
        'symptoms': disease_data['Angina'],
        'recommendations': [
            'Seek immediate medical attention',
            'Rest when symptoms occur',
            'Avoid strenuous activity',
            'Manage stress',
            'Follow cardiac diet'
        ],
        'medications': [
            'Nitroglycerin for acute episodes',
            'Beta-blockers',
            'Calcium channel blockers',
            'Aspirin for prevention'
        ]
    },
    'diabetes': {
        'symptoms': disease_data['Diabetes'],
        'recommendations': [
            'Monitor blood sugar regularly',
            'Follow diabetic diet plan',
            'Exercise regularly',
            'Maintain healthy weight',
            'Attend regular checkups',
            'Check feet daily'
        ],
        'medications': [
            'Metformin',
            'Insulin therapy if needed',
            'GLP-1 agonists',
            'SGLT2 inhibitors',
            'Blood glucose monitoring supplies'
        ]
    },
    'hypoglycemia': {
        'symptoms': disease_data['Hypoglycemia'],
        'recommendations': [
            'Eat or drink fast-acting carbs immediately',
            'Check blood sugar after 15 minutes',
            'Eat regular meals',
            'Adjust medication if recurring',
            'Carry glucose tablets'
        ],
        'medications': [
            'Glucose tablets or gel',
            'Glucagon injection for emergencies',
            'Adjustment of diabetes medications',
            'Continuous glucose monitoring'
        ]
    },
    'anxiety': {
        'symptoms': disease_data['Anxiety'],
        'recommendations': [
            'Practice deep breathing and meditation',
            'Regular exercise and physical activity',
            'Limit caffeine and alcohol',
            'Talk to mental health professional',
            'Join support groups',
            'Maintain regular sleep schedule'
        ],
        'medications': [
            'SSRIs (Sertraline, Escitalopram)',
            'Benzodiazepines (short-term use only)',
            'Beta-blockers for physical symptoms',
            'Therapy and counseling (CBT)'
        ]
    },
    'depression': {
        'symptoms': disease_data['Depression'],
        'recommendations': [
            'Seek professional help',
            'Stay connected with loved ones',
            'Exercise regularly',
            'Maintain sleep routine',
            'Avoid alcohol and drugs',
            'Set small, achievable goals'
        ],
        'medications': [
            'SSRIs (Fluoxetine, Sertraline)',
            'SNRIs (Venlafaxine)',
            'Atypical antidepressants',
            'Psychotherapy (CBT, IPT)'
        ]
    },
    'urinary tract infection': {
        'symptoms': disease_data['Urinary Tract Infection'],
        'recommendations': [
            'Drink plenty of water',
            'Urinate frequently',
            'Complete full antibiotic course',
            'Avoid irritants (caffeine, alcohol)',
            'Use heating pad for pain'
        ],
        'medications': [
            'Antibiotics (Trimethoprim, Nitrofurantoin)',
            'Pain relievers (Phenazopyridine)',
            'Acetaminophen for fever',
            'Cranberry supplements (prevention)'
        ]
    },
    'strep throat': {
        'symptoms': disease_data['Strep Throat'],
        'recommendations': [
            'Complete full antibiotic course',
            'Rest and stay hydrated',
            'Gargle with salt water',
            'Use humidifier',
            'Avoid sharing utensils'
        ],
        'medications': [
            'Antibiotics (Penicillin, Amoxicillin)',
            'Pain relievers (Acetaminophen, Ibuprofen)',
            'Throat lozenges',
            'Throat sprays for numbing'
        ]
    },
    'arthritis': {
        'symptoms': disease_data['Arthritis'],
        'recommendations': [
            'Stay physically active',
            'Maintain healthy weight',
            'Apply heat or cold therapy',
            'Protect joints during activities',
            'Use assistive devices if needed'
        ],
        'medications': [
            'NSAIDs (Ibuprofen, Naproxen)',
            'Acetaminophen for pain',
            'DMARDs for rheumatoid arthritis',
            'Topical pain relievers'
        ]
    },
    'fibromyalgia': {
        'symptoms': disease_data['Fibromyalgia'],
        'recommendations': [
            'Develop sleep routine',
            'Exercise regularly (low-impact)',
            'Manage stress',
            'Pace activities',
            'Join support groups'
        ],
        'medications': [
            'Duloxetine (Cymbalta)',
            'Pregabalin (Lyrica)',
            'Pain relievers',
            'Sleep medications if needed'
        ]
    },
    'eczema': {
        'symptoms': disease_data['Eczema'],
        'recommendations': [
            'Moisturize skin regularly',
            'Avoid irritants and triggers',
            'Take lukewarm baths',
            'Use mild soaps',
            'Wear soft, breathable fabrics'
        ],
        'medications': [
            'Topical corticosteroids',
            'Moisturizing creams and ointments',
            'Antihistamines for itching',
            'Topical calcineurin inhibitors'
        ]
    },
    'psoriasis': {
        'symptoms': disease_data['Psoriasis'],
        'recommendations': [
            'Moisturize daily',
            'Avoid triggers (stress, cold)',
            'Get moderate sun exposure',
            'Avoid scratching',
            'Manage stress'
        ],
        'medications': [
            'Topical corticosteroids',
            'Vitamin D analogs',
            'Retinoids',
            'Biologics for severe cases'
        ]
    }
}

def create_training_dataset():
    """Create training dataset from disease-symptom mappings"""
    
    # Create rows for training
    rows = []
    
    for disease, symptoms in disease_data.items():
        # Create positive examples (disease with its symptoms)
        for i in range(5):  # Generate 5 samples per disease
            # Randomly select 3-7 symptoms
            import random
            num_symptoms = random.randint(3, min(7, len(symptoms)))
            selected_symptoms = random.sample(symptoms, num_symptoms)
            
            symptom_text = ' '.join(selected_symptoms)
            rows.append({
                'symptoms': symptom_text,
                'disease': disease
            })
    
    # Create DataFrame
    df = pd.DataFrame(rows)
    
    return df

if __name__ == '__main__':
    print("Creating training dataset...")
    
    # Create dataset
    df = create_training_dataset()
    
    # Save to CSV
    df.to_csv('data/training_data.csv', index=False)
    print(f"✓ Saved {len(df)} training samples to data/training_data.csv")
    
    # Save disease info
    joblib.dump(disease_info, 'data/disease_info.pkl')
    print(f"✓ Saved information for {len(disease_info)} diseases")
    
    print("\nDataset Statistics:")
    print(f"  Total samples: {len(df)}")
    print(f"  Number of diseases: {len(disease_data)}")
    print(f"  Diseases: {', '.join(list(disease_data.keys())[:5])}...")
