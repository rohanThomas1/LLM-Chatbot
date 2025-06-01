# LLM Chatbot with FastAPI + SQL + Groq

## Setup Instructions

1. Clone the repo to local
2. Create `.env` in the same folder with your GROQ_API_KEY from https://console.groq.com/home
3. Install dependencies: `pip install -r requirements.txt`
4. Create customer database: `python seed.py`
5. Start backend: `python -m uvicorn main:app --reload`
6. Create the API request in Postman (https://web.postman.co/) with local URL (http://127.0.0.1:8000/query)
