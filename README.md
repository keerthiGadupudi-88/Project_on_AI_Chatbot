# 🤖 Groq AI Chatbot

A simple and beginner-friendly AI chatbot built using **Python, Groq API, and Streamlit**.

The application allows users to enter questions and receive responses from a Groq Large Language Model (LLM). It also maintains the conversation history during the current Streamlit session.

---

## 🚀 Features

* 🤖 AI chatbot interface
* ⚡ Powered by Groq API
* 🐍 Built using Python
* 🎈 Simple Streamlit interface
* 💬 User can send multiple messages
* 🧠 Maintains conversation history during the session
* 🗑️ Clear Chat option
* 📱 Can be accessed through a web browser
* 🎓 Beginner-friendly project

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **Groq API**
* **Groq Python SDK**
* **OpenAI GPT-OSS-120B model through Groq**

---

## 📁 Project Structure

```text
groq_chatbot/
│
├── Chatbot.py
└── requirements.txt
```

---

## 📋 Requirements

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

Recommended:

```text
Python 3.10+
```

---

## 📦 Installation

### Step 1: Clone or download the project

If you are using GitHub:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Then open the project folder:

```bash
cd groq_chatbot
```

---

### Step 2: Install required libraries

Run:

```bash
python -m pip install streamlit groq
```

Or install everything using the requirements file:

```bash
python -m pip install -r requirements.txt
```

---

## 🔑 Groq API Key

You need a Groq API key to use the chatbot.

Open `Chatbot.py` and find:

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY_HERE"
```

Replace it with your Groq API key:

```python
GROQ_API_KEY = "your_api_key_here"
```

### ⚠️ Security Warning

Never upload your actual API key to GitHub or share it publicly.

For a real deployment, use Streamlit Secrets or environment variables instead of placing the API key directly in the Python file.

---

## ▶️ Running the Application

Open Command Prompt in the project folder:

```bash
cd "C:\Users\HP\OneDrive\Desktop\GEN AI"
```

Run the application:

```bash
python -m streamlit run Chatbot.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open this URL in your browser.

---

## 💬 How to Use

1. Open the chatbot in your browser.
2. Type a question in the chat box.
3. Press **Enter**.
4. The message is sent to the Groq LLM.
5. The AI response appears on the screen.
6. Continue asking questions.
7. The chatbot remembers previous messages during the current session.
8. Click **Clear Chat** to start a new conversation.

---

## 🧠 Conversation History

The chatbot uses Streamlit's session state:

```python
st.session_state.messages
```

User and assistant messages are stored during the current session.

Example:

```text
User:
What is Python?

AI:
Python is a high-level programming language...

User:
What is it used for?

AI:
Python is commonly used for web development,
data science, AI, automation, and more.
```

The previous conversation is sent to the Groq model so the chatbot can understand the context.

---

## 🤖 Model

The application uses:

```text
openai/gpt-oss-120b
```

through the Groq API.

The model name is specified in `Chatbot.py`:

```python
model="openai/gpt-oss-120b"
```

---

## 🧪 Testing

Try the following questions after starting the application:

### Test 1

```text
What is artificial intelligence?
```

### Test 2

```text
Explain Python in simple words.
```

### Test 3

```text
What is machine learning?
```

### Test 4

```text
Give me a simple Java program.
```

### Test 5

```text
What did I ask you previously?
```

The last test checks whether conversation history is working.

---

## 🗑️ Clear Chat

The sidebar contains a:

```text
🗑️ Clear Chat
```

button.

Clicking it removes the current conversation and starts a fresh chat.

---

## ❗ Common Errors

### Error: No module named 'groq'

Run:

```bash
python -m pip install groq
```

---

### Error: No module named 'streamlit'

Run:

```bash
python -m pip install streamlit
```

---

### Error: Model not found

Make sure the model name in `Chatbot.py` is a currently available Groq model.

For this project:

```python
model="openai/gpt-oss-120b"
```

---

### Streamlit command not recognized

Instead of:

```bash
streamlit run Chatbot.py
```

use:

```bash
python -m streamlit run Chatbot.py
```

---

## 📄 requirements.txt

The project requires:

```text
streamlit
groq
```

---

## 🔮 Future Improvements

The chatbot can be extended with:

* 🎤 Voice input
* 🔊 Text-to-speech responses
* 📄 PDF question answering
* 🖼️ Image understanding
* 🌐 Web search
* 💾 Chat history storage
* 🔐 Secure API key management
* 🎨 Advanced UI
* 📥 Download conversation
* 👤 User login system

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python API integration
* Using the Groq Python SDK
* Calling an LLM from Python
* Streamlit application development
* Chat interfaces
* Session state
* Conversation history
* Error handling
* Basic AI application development

---

## 👩‍💻 Author

**Keerthi Gadupudi**

Built using:

**Python + Groq API + Streamlit**

---

## ⭐ Conclusion

This project demonstrates how to build a simple AI chatbot using Python and the Groq API with a beginner-friendly Streamlit interface.

Run:

```bash
python -m streamlit run Chatbot.py
```

and start chatting with your AI assistant! 🤖
