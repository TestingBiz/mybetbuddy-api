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

        # Convert 'horses' JSONB field into a proper list
        for race in data:
            race["horses"] = json.loads(race["horses"])  # Convert stringified JSON to list

        return data

    except Exception as e:
        return {"error": str(e)}

