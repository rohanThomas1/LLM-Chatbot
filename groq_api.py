import logging
import httpx
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama3-8b-8192"

async def query_llm(user_query: str) -> str:
    prompt = f"""Generate a valid SQL SELECT query for the following user request.
    Use table name `customers` with columns: customer_id, name, gender, location.
    Only output the SQL query without any explanation or formatting.
    Request: {user_query}"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": MODEL
    }

    async with httpx.AsyncClient() as client:
        response = await client.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
        response.raise_for_status()
        
        response_data = response.json()        
        sql_raw = response.json()['choices'][0]['message']['content']
        
        # Extract only the SQL statement
        sql_lines = sql_raw.strip().splitlines()
        sql_query = next((line for line in sql_lines if line.strip().lower().startswith("select")), "").strip().rstrip(";")
        sql_query += ";"
        return sql_query
