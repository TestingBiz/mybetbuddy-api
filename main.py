import os
from supabase import create_client
from fastapi import FastAPI

app = FastAPI()

# Print environment variables for debugging
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

print(f"SUPABASE_URL: {SUPABASE_URL}")  # Debugging
print(f"SUPABASE_KEY: {SUPABASE_KEY[:5]}********")  # Debugging (partially hidden for security)

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running with Supabase!"}

@app.get("/races")
def get_races():
    response = supabase.table("races").select("*").execute()
    return response.data  # Ensure we return only the data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
