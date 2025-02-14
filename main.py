from fastapi import FastAPI
import os
from supabase import create_client

# Initialize FastAPI app
app = FastAPI()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

# NEW ENDPOINT: Fetch races from Supabase
@app.get("/races")
def get_races():
    response = supabase.table("races").select("*").execute()
    return response.data

