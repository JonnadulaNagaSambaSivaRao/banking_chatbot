# 🏦 Banking Assistant Chatbot 🤖

<p align="center">

<img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/LangChain-LLM-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/LangGraph-Agent-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Groq-Llama%20LLM-red?style=for-the-badge">
<img src="https://img.shields.io/badge/Database-SQLite-lightgrey?style=for-the-badge&logo=sqlite">

</p>


## 🚀 Project Overview

**Banking Assistant Chatbot** is an AI-powered conversational banking assistant built using:

✨ FastAPI  
✨ LangChain  
✨ LangGraph  
✨ Groq LLM  
✨ SQLite Database  
✨ UV Package Manager  

The chatbot understands banking-related queries and generates intelligent responses using Large Language Models.

The project demonstrates:

- 🔹 API development using FastAPI
- 🔹 LLM integration using Groq
- 🔹 Prompt Engineering
- 🔹 AI workflow management using LangGraph
- 🔹 Database storage using SQLite
- 🔹 Modern Python dependency management using UV


---

# 🎯 Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Banking Assistant | Answers banking-related questions |
| ⚡ FastAPI API | High-performance backend API |
| 🧠 LangChain Integration | Connects application with LLM |
| 🔄 LangGraph Workflow | Controls chatbot execution flow |
| 🗄 SQLite Database | Stores conversations |
| 🔐 Environment Security | API keys managed using `.env` |
| 📦 UV Management | Fast Python package management |


---

# 🏗️ System Architecture


```
                 User
                  |
                  |
                  v
          FastAPI Chat API
                  |
                  |
                  v
          LangGraph Workflow
                  |
                  |
                  v
            LangChain
                  |
                  |
                  v
            Groq Llama LLM
                  |
                  |
                  v
            SQLite Database

```


---

# 🛠️ Technology Stack


## Backend

- 🐍 Python
- 🚀 FastAPI
- ⚡ Uvicorn


## Artificial Intelligence

- 🧠 LangChain
- 🔄 LangGraph
- 🤖 Groq Llama Model


## Database

- 🗄 SQLite
- SQLAlchemy ORM


## Development Tools

- 📦 UV Package Manager
- 🔑 Python-dotenv
- 🔐 JWT Authentication Packages


---

# 📂 Project Structure


```
banking_chatbot

│
├── app
│   |
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   |
│   ├── routers
│   │       └── chatbot.py
│   |
│   ├── langchain
│   │       ├── llm.py
│   │       └── prompts.py
│   |
│   └── langgraph
│           └── workflow.py
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md

```


---

# ⚙️ Installation & Setup


## 1️⃣ Clone Repository


```bash
git clone https://github.com/yourusername/banking_chatbot.git

cd banking_chatbot
```


---

# 2️⃣ Initialize UV Environment


```powershell
uv init
```


Create virtual environment:


```powershell
uv venv
```


Activate:


```powershell
.venv\Scripts\activate
```


---

# 3️⃣ Install Dependencies


```powershell
uv add fastapi

uv add uvicorn

uv add langchain

uv add langgraph

uv add langchain-groq

uv add sqlalchemy

uv add python-dotenv

uv add python-jose passlib bcrypt

uv add pydantic
```


---

# 🔑 Environment Configuration


Create `.env` file:


```
GROQ_API_KEY=your_groq_api_key_here
```


⚠️ Never upload `.env` file to GitHub.


Add to `.gitignore`:


```
.env
__pycache__
.venv
```


---

# 🗄 Database Configuration


The project uses SQLite:


```
sqlite:///./banking.db
```


SQLAlchemy creates and manages database tables automatically.


---

# 🧠 LangChain LLM Configuration


The chatbot uses Groq Llama model:


```
Model:

llama-3.1-8b-instant
```


Workflow:


```
User Question
      |
      |
      v
Prompt Template
      |
      |
      v
Groq LLM
      |
      |
      v
AI Response

```


---

# 🔄 LangGraph Workflow


The chatbot workflow contains:

```
START

 |
 |
 v

Chatbot Node

 |
 |
 v

END

```


LangGraph manages the execution flow of the AI agent.


---

# ▶️ Running the Application


Start FastAPI server:


```powershell
uv run uvicorn app.main:app --reload
```


Server:


```
http://127.0.0.1:8000
```


API Documentation:


```
http://127.0.0.1:8000/docs
```


---

# 📡 API Usage


## Chat Endpoint


### POST

```
/chat
```


Example Request:


```
message:

"What are the types of bank accounts?"
```


Example Response:


```json
{
 "response":
 "Banks provide savings accounts, current accounts and fixed deposits."
}

```


---

# 📸 Application Flow


```
User enters banking question

        ↓

FastAPI receives request

        ↓

LangGraph processes workflow

        ↓

LangChain sends prompt

        ↓

Groq LLM generates answer

        ↓

Response returned to user

```


---

# 🔐 Security Practices


✅ API keys stored in `.env`

✅ Password hashing support

✅ JWT authentication packages included

✅ Sensitive files excluded from GitHub


---

# 🚀 Future Enhancements


✨ User authentication system

✨ Multiple bank account management

✨ Transaction history

✨ PDF mini statement generation

✨ Voice-based banking assistant

✨ RAG with banking documents

✨ Admin dashboard


---

# 👨‍💻 Developer


**Jonnadula Naga Samba Siva Rao**

AI | Full Stack Developer


---

# ⭐ Support

If you like this project, please ⭐ star the repository.

Happy Coding! 🚀
