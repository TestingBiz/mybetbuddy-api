from fastapi import FastAPI
from supabase import create_client
import os

app = FastAPI()

# Load Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Ensure Supabase credentials exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/races")
def get_races():
    """ Fetch all races with related horses from Supabase """
    try:
        # Fetch races
        races_response = supabase.table("races").select("id, date, location").execute()
        races = races_response.data

        if not races:
            return {"message": "No races found"}

        # Fetch horses linked to each race
        for race in races:
            race_id = race["id"]
            horses_response = (
                supabase.table("horses")
                .select("horse, trainer, jockey, owner, age, sex, weight, draw, sire, dam")
                .eq("race_id", race_id)
                .execute()
            )
            race["horses"] = horses_response.data  # Attach horses to each race

        return {"races": races}

    except Exception as e:
        return {"error": str(e)}
