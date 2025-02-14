from fastapi import FastAPI
import os
from supabase import create_client
import json

app = FastAPI()

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/races")
def get_races():
    try:
        response = supabase.table("races").select("id, date, location, horses").execute()
        data = response.data

        # Ensure 'horses' JSONB field is **properly parsed** into a structured list
        for race in data:
            if isinstance(race["horses"], str):  # If it's still a string, convert it
                race["horses"] = json.loads(race["horses"])

        return data  # Cleanly formatted JSON

    except Exception as e:
        return {"error": str(e)}

