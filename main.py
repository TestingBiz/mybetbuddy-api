from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from supabase import create_client, Client

# Initialize FastAPI app
app = FastAPI()

# Get Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Ensure credentials are set
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/races")
def get_races():
    """
    Fetch all races from the Supabase 'races' table.
    Returns the data in a structured JSON response.
    """
    try:
        response = supabase.table("races").select("*").execute()
        return JSONResponse(content=response.data, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Run the app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Use environment PORT or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
