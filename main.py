from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

# Debugging: Print Supabase URL
print("SUPABASE_URL:", os.getenv("SUPABASE_URL"))

# Load Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/test-db")
def test_db():
    """Fetch some test data from Supabase."""
    response = supabase.table("your_table_name").select("*").execute()
    return response.data

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
