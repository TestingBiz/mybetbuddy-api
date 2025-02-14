import os
from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

# Retrieve Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/races")
def get_races():
    try:
        # Query the races table
        response = supabase.table("races").select("*").execute()
        data = response.data  

        return data  # FastAPI will automatically convert JSONB fields correctly

    except Exception as e:
        return {"error": str(e)}

