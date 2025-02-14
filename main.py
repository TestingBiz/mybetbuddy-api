import os
import json  # Using built-in json module
from fastapi import FastAPI
from supabase import create_client

app = FastAPI()

# Retrieve Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Ensure credentials exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/races")
def get_races():
    try:
        response = supabase.table("races").select("*").execute()
        
        # Extract data from the response
        data = response.data  

        # Return properly formatted JSON
        return json.loads(json.dumps(data))  

    except Exception as e:
        return {"error": str(e)}
