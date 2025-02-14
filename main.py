from fastapi import FastAPI
import os
from supabase import create_client

# Initialize FastAPI app
app = FastAPI()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Ensure Supabase credentials exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials! Check Railway environment variables.")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

# ✅ NEW ENDPOINT: Fetch races from Supabase
@app.get("/Races")
def get_Races():
    response = supabase.table("Races").select("*").execute()
    return response.data

