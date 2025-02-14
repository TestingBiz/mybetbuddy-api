from fastapi import FastAPI
import os
from supabase import create_client

app = FastAPI()

# Load Supabase credentials from Railway environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/trainers")
def get_trainers():
    """Fetch trainers from Supabase."""
    response = supabase.table("trainers").select("*").execute()
    return response.data

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Use PORT from env or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)

