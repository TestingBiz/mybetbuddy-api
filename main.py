from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

# Load environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Ensure credentials exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("🚨 Missing Supabase credentials! Check Railway environment variables.")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/races")
def get_races():
    try:
        # ✅ Corrected: Using "Races" with capital R
        response = supabase.table("Races").select("*").execute()
        data = response.data  # Extract actual data from Supabase response
        print("✅ Successfully fetched races:", data)  # Debugging log
        return data
    except Exception as e:
        print("❌ Error fetching races:", str(e))  # Debugging log
        return {"error": str(e)}

