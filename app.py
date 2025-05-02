from flask import Flask, request, jsonify, render_template
from googlesearch import search
import uuid
import sys
from io import StringIO
import json

app = Flask(__name__)

# Simulated learner profile (in production, use a database)
learner_profile = {
    'skill_level': 'beginner',
    'completed_exercises': [],
    'performance_history': [],
    'preferred_topics': ['patient data analysis', 'basic statistics']
}

class LearningAgent:
    def __init__(self):
        self.memory = []
        self.max_memory = 10
        self.reward_history = []

    def validate_input(self, input_text):
        banned_words = ['eval', 'exec', 'import os', 'import sys', '__']
        return not any(word in input_text.lower() for word in banned_words)

    def process_input(self, input_text):
        if not self.validate_input(input_text):
            return {'type': 'error', 'content': 'Input contains restricted content. Please avoid using system-level commands.'}

        self.memory.append({'role': 'user', 'content': input_text})
        if len(self.memory) > self.max_memory:
            self.memory.pop(0)

        reasoning_steps = []
        intent = self.detect_intent(input_text)
        reasoning_steps.append(f"Detected intent: {intent}")

        if intent == 'question':
            response = self.handle_question(input_text)
        elif intent == 'exercise':
            response = self.handle_exercise()
        elif intent == 'code_submission':
            response = self.handle_code_submission(input_text)
        else:
            response = {'content': 'Please ask a question, request an exercise, or submit code.'}

        reward = self.calculate_reward(response)
        self.reward_history.append(reward)
        self.adjust_learning_path(reward)

        return {'type': 'agent', 'content': response['content'], 'reasoning': '\n'.join(reasoning_steps)}

    def detect_intent(self, input_text):
        input_lower = input_text.lower()
        if 'exercise' in input_lower or 'practice' in input_lower:
            return 'exercise'
        elif 'def ' in input_text or 'print(' in input_text:
            return 'code_submission'
        else:
            return 'question'

    def handle_question(self, input_text):
        if 'explain' in input_text.lower() or 'how to' in input_text.lower():
            try:
                results = list(search(input_text, num_results=1))
                return {'content': f"Based on web search: {results[0] if results else 'No results found'}"}
            except Exception as e:
                return {'content': f"Web search failed: {str(e)}. Fallback: For example, to calculate average heart rate, use a list comprehension in Python."}
        return {'content': 'For example, to calculate average heart rate, use a list comprehension in Python.'}

    def handle_exercise(self):
        difficulty = 'easy' if learner_profile['skill_level'] == 'beginner' else 'medium'
        exercise = self.generate_exercise(difficulty)
        return {'content': exercise}

    def handle_code_submission(self, code):
        try:
            # Use Pyodide for safe code execution (simulated here, as Pyodide runs in browser)
            old_stdout = sys.stdout
            redirected_output = sys.stdout = StringIO()
            exec(code, {'__builtins__': {}}, {})
            sys.stdout = old_stdout
            output = redirected_output.getvalue()
            learner_profile['completed_exercises'].append({'code': code, 'result': output})
            return {'content': f"Code executed successfully! Output: {output or 'No output'}"}
        except Exception as e:
            return {'content': f"Error in code: {str(e)}. Here's a hint: Check your syntax."}

    def generate_exercise(self, difficulty):
        if difficulty == 'easy':
            return """
Please write a Python function to calculate the average heart rate from a list of readings.
Example input: [70, 72, 68, 74]
Expected output: 71
            """
        return """
Please write a Python function to analyze patient blood pressure readings and flag abnormal values.
Example input: [(120, 80), (130, 85), (150, 100)]
Expected output: "High blood pressure detected: (150, 100)"
        """

    def calculate_reward(self, response):
        return 1 if 'successfully' in response['content'].lower() else -1

    def adjust_learning_path(self, reward):
        recent_rewards = self.reward_history[-3:]
        if recent_rewards:
            average_reward = sum(recent_rewards) / len(recent_rewards)
            if average_reward > 0.5 and learner_profile['skill_level'] == 'beginner':
                learner_profile['skill_level'] = 'intermediate'

agent = LearningAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    user_input = data.get('input', '')
    response = agent.process_input(user_input)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)