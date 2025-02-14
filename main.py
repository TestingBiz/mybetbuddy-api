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
        # Explicitly select fields
        response = supabase.table("races").select("id, date, location, horses").execute()
        data = response.data

        # Ensure JSONB column is parsed correctly
        for race in data:
            if isinstance(race["horses"], str):  # If it's still a string, convert it
                try:
                    race["horses"] = json.loads(race["horses"])
                except json.JSONDecodeError:
                    pass  # If decoding fails, keep it as is

        return {"races": data}

    except Exception as e:
        return {"error": str(e)}

