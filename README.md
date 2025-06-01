# LLM Chatbot with FastAPI + SQL + Groq

## Setup Instructions

1. Clone the repo
2. Create `.env` with your GROQ_API_KEY from https://console.groq.com/home
3. Install dependencies:
```bash pip install -r requirements.txt```
4. Create the customer database by running `python seed.py`
5. Start the backend using `python -m uvicorn main:app --reload`
6. Install Postman agent to make local API request (http://127.0.0.1:8000/query), and create the API request in Postman (https://web.postman.co/)
