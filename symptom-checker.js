// ============================================
// MediSense AI - Symptom Checker Logic
// ============================================

// Symptom categories and options
const symptomCategories = {
    'General': [
        'Fever', 'Chills', 'Fatigue', 'Weakness', 'Weight Loss', 'Night Sweats'
    ],
    'Head & Neurological': [
        'Headache', 'Dizziness', 'Confusion', 'Memory Problems', 'Visual Disturbances', 'Sensitivity to Light'
    ],
    'Respiratory': [
        'Cough', 'Shortness of Breath', 'Wheezing', 'Chest Pain', 'Sore Throat', 'Runny Nose', 'Sneezing', 'Congestion'
    ],
    'Cardiovascular': [
        'Rapid Heartbeat', 'Irregular Heartbeat', 'Chest Pressure', 'Palpitations', 'Swelling in Legs'
    ],
    'Digestive': [
        'Nausea', 'Vomiting', 'Diarrhea', 'Abdominal Pain', 'Bloating', 'Loss of Appetite', 'Constipation'
    ],
    'Muscular & Skeletal': [
        'Muscle Aches', 'Joint Pain', 'Back Pain', 'Stiffness', 'Weakness in Limbs'
    ],
    'Mental & Emotional': [
        'Anxiety', 'Excessive Worry', 'Restlessness', 'Difficulty Concentrating', 'Sleep Problems', 'Mood Changes'
    ],
    'Skin': [
        'Rash', 'Itching', 'Dry Skin', 'Hives', 'Skin Discoloration'
    ],
    'Eyes, Ears, Nose, Throat': [
        'Itchy Eyes', 'Watery Eyes', 'Ear Pain', 'Hearing Problems', 'Nasal Congestion', 'Loss of Smell'
    ],
    'Urinary': [
        'Frequent Urination', 'Painful Urination', 'Dark Urine', 'Blood in Urine'
    ],
    'Other': [
        'Dehydration', 'Excessive Thirst', 'Sweating', 'Tingling in Hands', 'Slow Healing', 'Swollen Glands'
    ]
};

// Initialize symptom checker
document.addEventListener('DOMContentLoaded', () => {
    renderSymptomCategories();

    const form = document.getElementById('symptom-form');
    if (form) {
        form.addEventListener('submit', handleSubmit);
    }
});

// Render symptom categories
function renderSymptomCategories() {
    const container = document.getElementById('symptom-categories');
    if (!container) return;

    for (const [category, symptoms] of Object.entries(symptomCategories)) {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'symptom-category';
        categoryDiv.style.marginBottom = '2rem';

        // Category header
        const header = document.createElement('h3');
        header.textContent = category;
        header.style.color = 'var(--primary-blue)';
        header.style.marginBottom = '1rem';
        categoryDiv.appendChild(header);

        // Symptom checkboxes
        const checkboxGroup = document.createElement('div');
        checkboxGroup.className = 'checkbox-group';

        symptoms.forEach(symptom => {
            const checkboxItem = document.createElement('label');
            checkboxItem.className = 'checkbox-item';

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.name = 'symptoms';
            checkbox.value = symptom.toLowerCase();
            checkbox.id = `symptom-${symptom.toLowerCase().replace(/\s+/g, '-')}`;

            const label = document.createElement('span');
            label.textContent = symptom;

            checkboxItem.appendChild(checkbox);
            checkboxItem.appendChild(label);
            checkboxGroup.appendChild(checkboxItem);
        });

        categoryDiv.appendChild(checkboxGroup);
        container.appendChild(categoryDiv);
    }
}

// Handle form submission
function handleSubmit(e) {
    e.preventDefault();

    // Get selected symptoms
    const checkboxes = document.querySelectorAll('input[name="symptoms"]:checked');
    const selectedSymptoms = Array.from(checkboxes).map(cb => cb.value);

    // Validate
    if (selectedSymptoms.length === 0) {
        alert('Please select at least one symptom to analyze.');
        return;
    }

    // Get duration and severity
    const duration = document.getElementById('duration').value;
    const severity = document.getElementById('severity').value;

    // Show loading state
    const submitBtn = document.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Analyzing...';
    submitBtn.disabled = true;

    // Simulate processing delay
    setTimeout(() => {
        // Navigate to results with selected symptoms
        showResults(selectedSymptoms);
    }, 1000);
}

// Clear all selections
function clearSelections() {
    const checkboxes = document.querySelectorAll('input[name="symptoms"]:checked');
    checkboxes.forEach(cb => cb.checked = false);

    document.getElementById('duration').value = '';
    document.getElementById('severity').value = '';
}
