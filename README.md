# 🎬 CODEFLIX AI

> **AI-powered GitHub Repository Intelligence Platform**

CODEFLIX AI helps developers understand unfamiliar GitHub repositories using AI. Simply provide a public GitHub repository URL, and CODEFLIX indexes the codebase, processes the repository, and allows users to ask natural-language questions about its architecture, files, logic, and implementation.

---

## 🚀 Live Demo

🌐 **Streamlit App: "https://codeflix-gpbdxzwznbzn8bshtmxots.streamlit.app/"

⚙️ **FastAPI Backend:"https://codeflix-backend-rvij.onrender.com"

📚 **API Documentation:"https://codeflix-backend-rvij.onrender.com/docs"

---

## ✨ Features

- 📂 **GitHub Repository Indexing**
  - Enter a public GitHub repository URL
  - Automatically clone and process the repository

- 🧠 **AI-Powered Code Understanding**
  - Ask questions about repository architecture
  - Understand project structure and code flow
  - Get explanations in natural language

- 🔍 **Repository-Aware Answers**
  - Answers are generated using relevant repository content
  - Source files are returned with AI responses

- 💬 **Conversation Memory**
  - Ask follow-up questions
  - Maintain context across the conversation

- ⚡ **FastAPI Backend**
  - REST API for repository indexing
  - REST API for repository-based chat

- 🎨 **Netflix-Inspired Interface**
  - Modern black-and-red UI
  - Interactive Streamlit frontend
  - Clean repository analysis experience

- ☁️ **Cloud Deployment**
  - Streamlit Community Cloud frontend
  - Render backend deployment

---

## 🏗️ Architecture

```text
┌──────────────────────┐
│      User            │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Streamlit Frontend  │
│  Netflix-Inspired UI │
└──────────┬───────────┘
           │
           │ REST API
           ▼
┌──────────────────────┐
│   FastAPI Backend    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  LangGraph Workflow  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ GitHub Repository    │
│ Loader               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Document Chunking    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Hugging Face         │
│ Embeddings API       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Chroma Vector Store  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ AI-Powered Answers   │
│ + Source Files       │
└──────────────────────┘
