// ============================================
// MediSense AI - Core JavaScript
// ============================================

// Dark Mode Toggle
function initTheme() {
  const savedTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);
}

function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';

  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.innerHTML = theme === 'light' ? '🌙' : '☀️';
  }
}

// Initialize theme on page load
document.addEventListener('DOMContentLoaded', () => {
  initTheme();

  // Add event listener to theme toggle
  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }
});

// ============================================
// Mock Disease Prediction Engine
// ============================================

const diseaseDatabase = {
  'common cold': {
    symptoms: ['runny nose', 'sore throat', 'cough', 'sneezing', 'congestion', 'headache', 'fatigue', 'mild fever'],
    recommendations: [
      'Get plenty of rest and sleep',
      'Stay hydrated by drinking lots of fluids',
      'Use a humidifier to ease congestion',
      'Gargle with salt water for sore throat',
      'Avoid smoking and secondhand smoke'
    ],
    medications: [
      'Acetaminophen (Tylenol) for fever and pain',
      'Decongestants (Pseudoephedrine) for congestion',
      'Cough suppressants (Dextromethorphan)',
      'Vitamin C and Zinc supplements'
    ]
  },
  'flu': {
    symptoms: ['high fever', 'chills', 'muscle aches', 'fatigue', 'cough', 'sore throat', 'headache', 'body aches', 'weakness'],
    recommendations: [
      'Rest and avoid physical exertion',
      'Stay home to prevent spreading infection',
      'Drink plenty of fluids',
      'Monitor fever and seek help if very high',
      'Use cool compresses for fever'
    ],
    medications: [
      'Antiviral medications (Tamiflu, Relenza)',
      'Acetaminophen or Ibuprofen for fever',
      'Decongestants for congestion',
      'Cough medicine (Dextromethorphan)'
    ]
  },
  'pneumonia': {
    symptoms: ['high fever', 'cough', 'chest pain', 'shortness of breath', 'fatigue', 'sweating', 'chills', 'rapid breathing'],
    recommendations: [
      'Seek immediate medical attention',
      'Complete full course of antibiotics',
      'Rest and conserve energy',
      'Stay hydrated',
      'Use humidifier for breathing comfort'
    ],
    medications: [
      'Antibiotics (prescribed by doctor)',
      'Fever reducers (Acetaminophen)',
      'Cough medicine if prescribed',
      'Pain relievers for chest pain'
    ]
  },
  'bronchitis': {
    symptoms: ['cough', 'mucus production', 'chest discomfort', 'fatigue', 'shortness of breath', 'mild fever', 'wheezing'],
    recommendations: [
      'Get plenty of rest',
      'Drink warm fluids',
      'Use humidifier',
      'Avoid irritants like smoke',
      'Practice breathing exercises'
    ],
    medications: [
      'Cough suppressants',
      'Bronchodilators if wheezing',
      'Antibiotics only if bacterial',
      'Pain relievers for discomfort'
    ]
  },
  'allergies': {
    symptoms: ['sneezing', 'runny nose', 'itchy eyes', 'watery eyes', 'congestion', 'skin rash', 'itching', 'scratchy throat'],
    recommendations: [
      'Identify and avoid allergen triggers',
      'Keep windows closed during high pollen days',
      'Use air purifiers indoors',
      'Shower after being outdoors',
      'Wash bedding regularly in hot water'
    ],
    medications: [
      'Antihistamines (Cetirizine, Loratadine)',
      'Nasal corticosteroid sprays (Flonase)',
      'Decongestants for congestion',
      'Eye drops for itchy eyes'
    ]
  },
  'asthma': {
    symptoms: ['shortness of breath', 'wheezing', 'chest tightness', 'cough', 'difficulty breathing', 'rapid breathing'],
    recommendations: [
      'Use inhaler as prescribed',
      'Avoid triggers (smoke, allergens)',
      'Monitor peak flow regularly',
      'Have action plan for attacks',
      'Exercise with doctor guidance'
    ],
    medications: [
      'Rescue inhaler (Albuterol)',
      'Controller medications (Inhaled corticosteroids)',
      'Long-acting bronchodilators',
      'Leukotriene modifiers'
    ]
  },
  'gastroenteritis': {
    symptoms: ['nausea', 'vomiting', 'diarrhea', 'abdominal pain', 'stomach cramps', 'fever', 'dehydration', 'loss of appetite'],
    recommendations: [
      'Stay hydrated with electrolyte solutions',
      'Eat bland foods (BRAT diet: bananas, rice, applesauce, toast)',
      'Rest and avoid solid foods initially',
      'Practice good hand hygiene',
      'Avoid dairy temporarily'
    ],
    medications: [
      'Oral rehydration solutions (Pedialyte)',
      'Anti-nausea medications (Ondansetron)',
      'Probiotics for recovery',
      'Avoid anti-diarrheal meds unless prescribed'
    ]
  },
  'food poisoning': {
    symptoms: ['nausea', 'vomiting', 'diarrhea', 'abdominal cramps', 'fever', 'weakness', 'headache', 'dehydration'],
    recommendations: [
      'Stay hydrated',
      'Rest and let body recover',
      'Avoid solid foods until nausea subsides',
      'Practice food safety in future',
      'Seek medical help if severe'
    ],
    medications: [
      'Oral rehydration solutions',
      'Anti-nausea medication if prescribed',
      'Electrolyte replacement drinks',
      'Antibiotics only if bacterial (prescribed)'
    ]
  },
  'acid reflux': {
    symptoms: ['heartburn', 'chest pain', 'difficulty swallowing', 'regurgitation', 'sour taste', 'cough', 'sore throat'],
    recommendations: [
      'Avoid trigger foods (spicy, acidic)',
      'Eat smaller, frequent meals',
      'Avoid lying down after eating',
      'Elevate head while sleeping',
      'Maintain healthy weight'
    ],
    medications: [
      'Antacids (Tums, Rolaids)',
      'H2 blockers (Famotidine)',
      'Proton pump inhibitors (Omeprazole)',
      'Alginates for coating stomach'
    ]
  },
  'irritable bowel syndrome': {
    symptoms: ['abdominal pain', 'bloating', 'gas', 'diarrhea', 'constipation', 'cramping', 'mucus in stool'],
    recommendations: [
      'Follow low-FODMAP diet',
      'Manage stress levels',
      'Exercise regularly',
      'Keep food diary',
      'Eat regular meals'
    ],
    medications: [
      'Antispasmodics for cramping',
      'Fiber supplements',
      'Anti-diarrheal medications',
      'Laxatives if constipated'
    ]
  },
  'migraine': {
    symptoms: ['severe headache', 'nausea', 'vomiting', 'sensitivity to light', 'sensitivity to sound', 'visual disturbances', 'dizziness', 'throbbing pain'],
    recommendations: [
      'Rest in a quiet, dark room',
      'Apply cold compress to forehead',
      'Avoid triggers like bright lights and loud sounds',
      'Practice relaxation techniques',
      'Maintain regular sleep schedule'
    ],
    medications: [
      'Triptans (Sumatriptan, Rizatriptan)',
      'NSAIDs (Ibuprofen, Naproxen)',
      'Anti-nausea medications',
      'Preventive medications if frequent'
    ]
  },
  'tension headache': {
    symptoms: ['headache', 'tightness around head', 'pressure in forehead', 'neck pain', 'shoulder pain', 'mild sensitivity to light'],
    recommendations: [
      'Rest and relax',
      'Apply heat or cold to affected area',
      'Massage neck and shoulders',
      'Practice stress management',
      'Maintain good posture'
    ],
    medications: [
      'Acetaminophen (Tylenol)',
      'Ibuprofen (Advil)',
      'Combination pain relievers',
      'Muscle relaxants if needed'
    ]
  },
  'hypertension': {
    symptoms: ['headache', 'dizziness', 'blurred vision', 'chest pain', 'shortness of breath', 'fatigue', 'irregular heartbeat', 'nosebleeds'],
    recommendations: [
      'Reduce sodium intake in diet',
      'Exercise regularly (30 minutes daily)',
      'Maintain healthy weight',
      'Limit alcohol consumption',
      'Quit smoking',
      'Monitor blood pressure regularly'
    ],
    medications: [
      'ACE inhibitors (Lisinopril, Enalapril)',
      'Beta-blockers (Metoprolol)',
      'Calcium channel blockers',
      'Diuretics (water pills)'
    ]
  },
  'angina': {
    symptoms: ['chest pain', 'chest pressure', 'shortness of breath', 'pain in arms', 'pain in neck', 'sweating', 'nausea', 'fatigue'],
    recommendations: [
      'Seek immediate medical attention',
      'Rest when symptoms occur',
      'Avoid strenuous activity',
      'Manage stress effectively',
      'Follow cardiac-healthy diet'
    ],
    medications: [
      'Nitroglycerin for acute episodes',
      'Beta-blockers',
      'Calcium channel blockers',
      'Aspirin for prevention'
    ]
  },
  'diabetes': {
    symptoms: ['frequent urination', 'excessive thirst', 'extreme hunger', 'fatigue', 'blurred vision', 'slow healing', 'tingling in hands', 'tingling in feet', 'weight loss'],
    recommendations: [
      'Monitor blood sugar levels regularly',
      'Follow a balanced, low-sugar diet',
      'Exercise regularly',
      'Maintain healthy weight',
      'Attend regular checkups',
      'Check feet daily for injuries'
    ],
    medications: [
      'Metformin',
      'Insulin therapy if needed',
      'GLP-1 agonists',
      'SGLT2 inhibitors',
      'Blood glucose monitoring supplies'
    ]
  },
  'hypoglycemia': {
    symptoms: ['shakiness', 'sweating', 'rapid heartbeat', 'dizziness', 'hunger', 'irritability', 'confusion', 'pale skin'],
    recommendations: [
      'Eat or drink fast-acting carbs immediately',
      'Check blood sugar after 15 minutes',
      'Eat regular meals and snacks',
      'Adjust medication if recurring',
      'Carry glucose tablets always'
    ],
    medications: [
      'Glucose tablets or gel',
      'Glucagon injection for emergencies',
      'Adjustment of diabetes medications',
      'Continuous glucose monitoring device'
    ]
  },
  'anxiety': {
    symptoms: ['excessive worry', 'restlessness', 'rapid heartbeat', 'sweating', 'trembling', 'difficulty concentrating', 'sleep problems', 'fatigue', 'irritability'],
    recommendations: [
      'Practice deep breathing and meditation',
      'Regular exercise and physical activity',
      'Limit caffeine and alcohol',
      'Talk to a mental health professional',
      'Join support groups',
      'Maintain regular sleep schedule'
    ],
    medications: [
      'SSRIs (Sertraline, Escitalopram)',
      'Benzodiazepines (for short-term use)',
      'Beta-blockers for physical symptoms',
      'Therapy and counseling (CBT)'
    ]
  },
  'depression': {
    symptoms: ['persistent sadness', 'loss of interest', 'fatigue', 'sleep problems', 'appetite changes', 'difficulty concentrating', 'feelings of worthlessness', 'hopelessness'],
    recommendations: [
      'Seek professional mental health support',
      'Stay connected with loved ones',
      'Exercise regularly',
      'Maintain consistent sleep routine',
      'Avoid alcohol and recreational drugs',
      'Set small, achievable daily goals'
    ],
    medications: [
      'SSRIs (Fluoxetine, Sertraline)',
      'SNRIs (Venlafaxine, Duloxetine)',
      'Atypical antidepressants',
      'Psychotherapy (CBT, IPT)'
    ]
  },
  'urinary tract infection': {
    symptoms: ['frequent urination', 'painful urination', 'burning sensation', 'cloudy urine', 'strong urine odor', 'pelvic pain', 'lower back pain', 'fever'],
    recommendations: [
      'Drink plenty of water',
      'Urinate frequently, don\'t hold it',
      'Complete full antibiotic course',
      'Avoid irritants (caffeine, alcohol, spicy foods)',
      'Use heating pad for pain relief'
    ],
    medications: [
      'Antibiotics (Trimethoprim, Nitrofurantoin)',
      'Pain relievers (Phenazopyridine)',
      'Acetaminophen for fever',
      'Cranberry supplements (prevention)'
    ]
  },
  'strep throat': {
    symptoms: ['severe sore throat', 'painful swallowing', 'fever', 'red tonsils', 'white patches', 'swollen lymph nodes', 'headache', 'rash'],
    recommendations: [
      'Complete full antibiotic course',
      'Rest and stay well hydrated',
      'Gargle with warm salt water',
      'Use humidifier to add moisture',
      'Avoid sharing utensils or drinks'
    ],
    medications: [
      'Antibiotics (Penicillin, Amoxicillin)',
      'Pain relievers (Acetaminophen, Ibuprofen)',
      'Throat lozenges for comfort',
      'Throat sprays for numbing pain'
    ]
  },
  'arthritis': {
    symptoms: ['joint pain', 'joint stiffness', 'swelling', 'reduced range of motion', 'redness', 'warmth in joints', 'fatigue'],
    recommendations: [
      'Stay physically active with low-impact exercise',
      'Maintain healthy weight',
      'Apply heat or cold therapy',
      'Protect joints during activities',
      'Use assistive devices if needed'
    ],
    medications: [
      'NSAIDs (Ibuprofen, Naproxen)',
      'Acetaminophen for pain',
      'DMARDs for rheumatoid arthritis',
      'Topical pain relievers (creams, gels)'
    ]
  },
  'fibromyalgia': {
    symptoms: ['widespread pain', 'fatigue', 'sleep problems', 'cognitive difficulties', 'headaches', 'mood issues', 'numbness', 'tingling'],
    recommendations: [
      'Develop consistent sleep routine',
      'Exercise regularly (low-impact activities)',
      'Manage stress with relaxation techniques',
      'Pace activities to avoid overexertion',
      'Join fibromyalgia support groups'
    ],
    medications: [
      'Duloxetine (Cymbalta)',
      'Pregabalin (Lyrica)',
      'Pain relievers (NSAIDs)',
      'Sleep medications if needed'
    ]
  },
  'eczema': {
    symptoms: ['itchy skin', 'red patches', 'dry skin', 'thickened skin', 'small bumps', 'oozing', 'crusting'],
    recommendations: [
      'Moisturize skin regularly and generously',
      'Avoid irritants and identified triggers',
      'Take lukewarm (not hot) baths',
      'Use mild, fragrance-free soaps',
      'Wear soft, breathable cotton fabrics'
    ],
    medications: [
      'Topical corticosteroids',
      'Moisturizing creams and ointments',
      'Antihistamines for itching',
      'Topical calcineurin inhibitors'
    ]
  },
  'psoriasis': {
    symptoms: ['red patches', 'silvery scales', 'dry skin', 'itching', 'burning', 'thick skin', 'joint pain'],
    recommendations: [
      'Moisturize skin daily',
      'Avoid triggers (stress, cold, infections)',
      'Get moderate sun exposure',
      'Avoid scratching affected areas',
      'Manage stress through relaxation'
    ],
    medications: [
      'Topical corticosteroids',
      'Vitamin D analogs',
      'Topical retinoids',
      'Biologics for severe cases'
    ]
  }
};

// Predict disease based on symptoms
function predictDisease(symptoms) {
  const results = [];

  // Convert symptoms to lowercase for matching
  const userSymptoms = symptoms.map(s => s.toLowerCase().trim());

  // Calculate match score for each disease
  for (const [disease, data] of Object.entries(diseaseDatabase)) {
    let matchCount = 0;

    for (const symptom of userSymptoms) {
      if (data.symptoms.some(ds => ds.includes(symptom) || symptom.includes(ds))) {
        matchCount++;
      }
    }

    if (matchCount > 0) {
      const confidence = (matchCount / data.symptoms.length) * 100;
      results.push({
        disease: disease.charAt(0).toUpperCase() + disease.slice(1),
        confidence: Math.min(confidence, 95), // Cap at 95%
        matchedSymptoms: matchCount,
        totalSymptoms: data.symptoms.length,
        recommendations: data.recommendations,
        medications: data.medications
      });
    }
  }

  // Sort by confidence
  results.sort((a, b) => b.confidence - a.confidence);

  // Return top 3 results
  return results.slice(0, 3);
}

// Store prediction results for results page
function storePrediction(results) {
  localStorage.setItem('predictionResults', JSON.stringify(results));
}

// Get stored prediction results
function getPrediction() {
  const stored = localStorage.getItem('predictionResults');
  return stored ? JSON.parse(stored) : null;
}

// Navigate to results page
function showResults(symptoms) {
  const predictions = predictDisease(symptoms);
  storePrediction(predictions);
  window.location.href = 'results.html';
}

// ============================================
// Utility Functions
// ============================================

// Smooth scroll to section
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Format confidence percentage
function formatConfidence(confidence) {
  return `${Math.round(confidence)}%`;
}

// Animate confidence bar
function animateConfidenceBar(element, targetWidth) {
  setTimeout(() => {
    element.style.width = targetWidth + '%';
  }, 100);
}
