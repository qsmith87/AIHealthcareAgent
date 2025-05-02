function sendMessage() {
    const input = document.getElementById('user-input').value;
    if (!input.trim()) return;

    appendMessage('user', input);
    document.getElementById('user-input').value = '';

    axios.post('/process', { input: input })
        .then(response => {
            appendMessage(response.data.type, response.data.content);
        })
        .catch(error => {
            appendMessage('error', 'Error communicating with server: ' + error.message);
        });
}

function appendMessage(type, content) {
    const output = document.getElementById('chat-output');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}-message`;
    messageDiv.textContent = content;
    output.appendChild(messageDiv);
    output.scrollTop = output.scrollHeight;
}

// Initialize with welcome message
appendMessage('agent', 'Welcome to the Healthcare Python Learning Companion! Ask a question, request an exercise, or submit Python code to learn data analysis for healthcare.');