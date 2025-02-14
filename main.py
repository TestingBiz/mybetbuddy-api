from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client
import os
import json

# ✅ Initialize FastAPI
app = FastAPI()

# ✅ Allow cross-origin requests (important for Bolt.ai & frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check your environment variables.")

# ✅ Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Fetch races from Supabase (UPDATED FIX)
def get_races_from_supabase():
    try:
        response = supabase.table("races").select("id, date, location, horses (horse, trainer, jockey, owner, age, sex, weight, draw, sire, dam)").execute()
        races = response.data  # Extract data correctly
        return races
    except Exception as e:
        raise ValueError(f"❌ Supabase API Error: {str(e)}")

# ✅ API Endpoint: Fetch all races
@app.get("/races")
def get_races():
    try:
        races = get_races_from_supabase()
        formatted_json = json.dumps({"races": races}, indent=4)  # Adds proper indentation
        return JSONResponse(content=formatted_json, media_type="application/json")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# ✅ Root route
@app.get("/")
def root():
    return {"message": "MyBetBuddy API is running!"}
