from fastapi import FastAPI
import os
from supabase import create_client

# Initialize FastAPI
app = FastAPI()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Validate Supabase credentials
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/races")  # ✅ Make sure this matches your test URL
def get_races():
    try:
        response = supabase.table("Races").select("*").execute()  # ✅ Ensure "Races" matches Supabase
        return response.data
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Get the PORT from environment
    uvicorn.run(app, host="0.0.0.0", port=port)

