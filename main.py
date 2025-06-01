from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import get_db, execute_query
from groq_api import query_llm
import logging
import os
from datetime import datetime

# Create log directory if it doesn't exist
log_dir = "log_files"
os.makedirs(log_dir, exist_ok=True)

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create log file with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"llm_chatbot_log_{timestamp}.log")

# Logging Configuration
logging.basicConfig(level=logging.INFO, 
                    format="%(asctime)s [%(levelname)s] %(message)s", 
                    handlers=[logging.FileHandler(log_file), 
                    logging.StreamHandler()])

class QueryRequest(BaseModel):
    user_query: str

@app.post("/query")
async def handle_query(request: QueryRequest):
    try:
        logging.info(f"Received query: {request.user_query}")
        sql_query = await query_llm(request.user_query)
        #print("Executing SQL:\n", sql_query)
        logging.info(f"Generated SQL: {sql_query}")
        results = execute_query(sql_query)
        return {"results": results}
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process query")
