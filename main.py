from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

# Load Supabase credentials from environment variables
SUPABASE_URL = os.getenv("https://jjxuctxvqgbigygmwdxx.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqeHVjdHh2cWdiaWd5Z213ZHh4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzkzMTUyNjUsImV4cCI6MjA1NDg5MTI2NX0.3QRlomjWXCiDfZRrBLavqIumYgDGclE1gO6a0CGSUtE")
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
