# LLM Chatbot with FastAPI + SQL + Groq

## Setup Instructions

1. Clone the repo
2. Create `.env` with your GROQ_API_KEY from https://console.groq.com/home
3. Install dependencies: `pip install -r requirements.txt`
4. Create the customer database: `python seed.py`
5. Start the backend: `python -m uvicorn main:app --reload`
6.a. Create the API request in Postman (https://web.postman.co/)
6.b. Install Postman agent to make local API request with URL http://127.0.0.1:8000/query
6.c. Under the Header tab, create a key:value pair 'Content-Type:application/json'
6.d. In the Body tab, select raw form with JSON as type
