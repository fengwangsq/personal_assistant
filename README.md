# Personal Assistant

A privacy-focused, offline virtual assistant running locally on your computer using Ollama and LangGraph.

## Features
- 🤖 Local AI powered by Ollama (llama3.2:3b-instruct-q4_K_M)
- 📁 File management (list, read, write files)
- 🔍 RAG document retrieval (ChromaDB)
- 🛡️ Complete privacy - all processing happens locally
- 💬 Modern chat interface

## Prerequisites
- Python 3.9+
- Node.js 18+
- Ollama installed with `llama3.2:3b-instruct-q4_K_M` model

## First Time Setup

### 1. Install Ollama Model
```bash
ollama pull llama3.2:3b-instruct-q4_K_M
```

### 2. Install Backend Dependencies
```bash
cd backend
python -m venv venv
# Activate virtual environment:
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Install Frontend Dependencies
```bash
cd frontend
npm install --legacy-peer-deps
```

## Starting the Personal Assistant

You need to start both the backend and frontend servers.

### Terminal 1: Start Backend
```bash
cd backend
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
uvicorn app.main:app --reload --port 8000
```
Backend will be available at `http://localhost:8000`

### Terminal 2: Start Frontend
```bash
cd frontend
npm run dev
```
Frontend will be available at `http://localhost:5173`

### 4. Open Your Browser
Navigate to `http://localhost:5173/` and start chatting with your assistant!

## Stopping the Personal Assistant

To stop the assistant, simply press **Ctrl+C** in each terminal window (both backend and frontend).

## Usage Examples

Try asking your assistant:
- "What files are in my current directory?"
- "Read the file README.md"
- "Create a new folder called 'documents'"
- "Write a file called 'notes.txt' with the content 'Hello World'"

## Troubleshooting

### Blank Page
If you see a blank page, ensure React and React-DOM are both version 18.3.1 in `frontend/package.json`, then:
```bash
cd frontend
npm install --legacy-peer-deps
npm run dev
```

### Backend Connection Error
Make sure Ollama is running and the model is downloaded:
```bash
ollama list  # Check installed models
ollama pull llama3.2:3b-instruct-q4_K_M  # Install if missing
```