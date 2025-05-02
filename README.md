The AI Healthcare Agent is an interactive web application designed for medical students to learn Python programming for healthcare data analysis. Powered by a ReAct-based agent, the application provides a chat interface where users can ask questions about Python in healthcare, request coding exercises, and submit Python code for execution and feedback. The agent adapts exercises to the user’s skill level using reinforcement learning, ensuring a personalized learning experience. Built with Flask, the project integrates RestrictedPython for safe code execution and googlesearch-python for answering queries, all optimized for development in PyCharm Community Edition.

Features





Interactive Chat Interface: Ask questions, request exercises, or submit Python code via a web-based chat.



Adaptive Learning: Exercises adjust in difficulty based on user performance, using a reinforcement learning reward system.



Safe Code Execution: User-submitted Python code is executed securely using RestrictedPython.



Web Search Integration: Answers to questions are enhanced with web search results (via googlesearch-python).



Error Handling: Robust validation and feedback for invalid inputs or code errors.



Minimal Frontend: Simple JavaScript for client-side interaction, compatible with PyCharm Community Edition’s limitations.

Prerequisites





Python 3.8+: Download from https://www.python.org/downloads/.



PyCharm Community Edition: Available at https://www.jetbrains.com/pycharm/download/.



Git: Install from https://git-scm.com/downloads/ for cloning the repository.



Web Browser: Chrome or Firefox for testing and debugging.



Internet Connection: Required for Axios CDN and web searches.

Setup Instructions

Follow these steps to set up and run the project locally.





Clone the Repository:





Open a terminal or PyCharm’s terminal (View > Tool Windows > Terminal).



Clone the repository:

git clone https://github.com/your-username/healthcare-python-learning-companion.git

Replace your-username with your GitHub username.



Navigate to the project directory:

cd healthcare-python-learning-companion



Create a Virtual Environment:





In PyCharm, go to File > Settings > Project > Python Interpreter.



Click the gear icon > Add Interpreter > Virtualenv Environment.



Create a new virtual environment (e.g., venv) in the project root.



Select the new interpreter and apply.



Alternatively, in the terminal:

python -m venv venv
.\venv\Scripts\activate



Install Dependencies:





Ensure the virtual environment is activated (you’ll see (venv) in the terminal).



Install dependencies from requirements.txt:

pip install -r requirements.txt



This installs Flask==2.3.3, googlesearch-python==1.2.4, and RestrictedPython==7.4.



Configure PyCharm Run Configuration:





Go to Run > Edit Configurations.



Add a new Python configuration:





Name: Flask App



Script path: Select app.py (e.g., C:\path\to\healthcare-python-learning-companion\app.py).



Environment variables: FLASK_ENV=development.



Python interpreter: Select the virtual environment.



Save the configuration.



Run the Application:





Click the green "Run" button in PyCharm or select the Flask App configuration.



The Flask server will start at http://127.0.0.1:5000.



Open a web browser and navigate to http://127.0.0.1:5000.

Usage





Ask Questions: Type queries like "How to calculate heart rate in Python?" to receive answers based on web searches or fallback responses.



Request Exercises: Enter "Give me an exercise" to get a Python coding challenge tailored to your skill level (beginner or intermediate).



Submit Code: Paste Python code (e.g., def calculate_average_heart_rate(rates): return sum(rates)/len(rates)) and click "Send" to execute it and see the output or error feedback.



The agent tracks your performance and adjusts exercise difficulty using reinforcement learning.
