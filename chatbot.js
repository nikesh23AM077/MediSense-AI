// ============================================
// MediSense AI - Chatbot Logic
// ============================================

let conversationState = {
    stage: 'greeting', // greeting, collecting, confirming, complete
    symptoms: [],
    messageHistory: []
};

// Initialize chatbot
document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const messagesContainer = document.getElementById('chat-messages');

    // Send welcome message
    addBotMessage("Hello! I'm your MediSense AI assistant. I'm here to help analyze your symptoms. Could you please describe what symptoms you're experiencing?");

    // Send message on button click
    if (sendBtn) {
        sendBtn.addEventListener('click', sendMessage);
    }

    // Send message on Enter key
    if (userInput) {
        userInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
});

// Send user message
function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();

    if (message === '') return;

    // Add user message to chat
    addUserMessage(message);

    // Clear input
    userInput.value = '';

    // Process message and generate response
    processUserMessage(message);
}

// Add bot message to chat
function addBotMessage(message) {
    const messagesContainer = document.getElementById('chat-messages');

    const messageDiv = document.createElement('div');
    messageDiv.className = 'message message-bot';

    messageDiv.innerHTML = `
    <div class="message-avatar">🤖</div>
    <div class="message-content">${message}</div>
  `;

    messagesContainer.appendChild(messageDiv);
    scrollToBottom();

    conversationState.messageHistory.push({ role: 'bot', message });
}

// Add user message to chat
function addUserMessage(message) {
    const messagesContainer = document.getElementById('chat-messages');

    const messageDiv = document.createElement('div');
    messageDiv.className = 'message message-user';

    messageDiv.innerHTML = `
    <div class="message-content">${message}</div>
    <div class="message-avatar">👤</div>
  `;

    messagesContainer.appendChild(messageDiv);
    scrollToBottom();

    conversationState.messageHistory.push({ role: 'user', message });
}

// Scroll to bottom of chat
function scrollToBottom() {
    const messagesContainer = document.getElementById('chat-messages');
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

// Process user message and generate response
function processUserMessage(message) {
    // Extract symptoms from message
    const extractedSymptoms = extractSymptoms(message);

    // Add to symptoms list
    conversationState.symptoms.push(...extractedSymptoms);

    // Generate response based on conversation stage
    setTimeout(() => {
        if (conversationState.stage === 'greeting') {
            conversationState.stage = 'collecting';

            if (extractedSymptoms.length === 0) {
                addBotMessage("I understand you're not feeling well. Can you tell me more specifically about your symptoms? For example, do you have fever, pain, nausea, or any other specific symptoms?");
            } else {
                const symptomsText = extractedSymptoms.join(', ');
                addBotMessage(`I see you're experiencing ${symptomsText}. Are there any other symptoms you'd like to mention? For example, how long have you had these symptoms?`);
            }
        } else if (conversationState.stage === 'collecting') {
            if (extractedSymptoms.length > 0) {
                addBotMessage("Thank you for sharing that information. Do you have any other symptoms you'd like to add, or should I analyze what you've told me so far?");
            } else if (message.toLowerCase().includes('no') || message.toLowerCase().includes('analyze') || message.toLowerCase().includes('that\'s all')) {
                conversationState.stage = 'confirming';
                confirmAndAnalyze();
            } else {
                addBotMessage("Could you describe any other symptoms? Or type 'no' if you've mentioned everything.");
            }
        } else if (conversationState.stage === 'confirming') {
            if (message.toLowerCase().includes('yes') || message.toLowerCase().includes('correct')) {
                addBotMessage("Perfect! I'm analyzing your symptoms now. Please wait a moment...");
                setTimeout(() => {
                    analyzeAndShowResults();
                }, 1500);
            } else {
                conversationState.stage = 'collecting';
                addBotMessage("No problem! Please tell me what other symptoms you have or what needs correction.");
            }
        }
    }, 800);
}

// Extract symptoms from user message
function extractSymptoms(message) {
    const symptoms = [];
    const lowerMessage = message.toLowerCase();

    // Common symptom keywords
    const symptomKeywords = [
        'fever', 'headache', 'cough', 'sore throat', 'runny nose', 'sneezing',
        'fatigue', 'tired', 'nausea', 'vomiting', 'diarrhea', 'pain', 'ache',
        'chills', 'dizzy', 'dizziness', 'weakness', 'congestion', 'stuffed nose',
        'body aches', 'muscle aches', 'chest pain', 'shortness of breath',
        'abdominal pain', 'stomach pain', 'sensitivity to light', 'blurred vision',
        'rapid heartbeat', 'sweating', 'anxiety', 'worry', 'restless',
        'itchy eyes', 'watery eyes', 'rash', 'dehydration', 'thirst',
        'frequent urination', 'tingling', 'slow healing', 'irregular heartbeat'
    ];

    symptomKeywords.forEach(keyword => {
        if (lowerMessage.includes(keyword)) {
            symptoms.push(keyword);
        }
    });

    // Remove duplicates
    return [...new Set(symptoms)];
}

// Confirm symptoms and prepare to analyze
function confirmAndAnalyze() {
    if (conversationState.symptoms.length === 0) {
        addBotMessage("I haven't detected any specific symptoms yet. Could you please describe what you're experiencing?");
        conversationState.stage = 'collecting';
        return;
    }

    const uniqueSymptoms = [...new Set(conversationState.symptoms)];
    const symptomsList = uniqueSymptoms.map(s => `• ${s}`).join('\n');

    addBotMessage(`Let me confirm the symptoms you've mentioned:\n\n${symptomsList}\n\nIs this correct? Type 'yes' to proceed with the analysis.`);
}

// Analyze symptoms and redirect to results
function analyzeAndShowResults() {
    const uniqueSymptoms = [...new Set(conversationState.symptoms)];

    if (uniqueSymptoms.length === 0) {
        addBotMessage("I need symptom information to provide an analysis. Could you please describe your symptoms?");
        conversationState.stage = 'collecting';
        return;
    }

    addBotMessage("Analysis complete! Redirecting you to your results...");

    // Use the prediction function from script.js
    setTimeout(() => {
        showResults(uniqueSymptoms);
    }, 1000);
}
