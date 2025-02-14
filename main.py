import os
from supabase import create_client
from fastapi import FastAPI

app = FastAPI()

# Load Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running with Supabase!"}

@app.get("/races")
def get_races():
    """ Fetch all races from the Supabase database and print debugging info """
    response = supabase.table("races").select("*").execute()
    
    print(f"🔍 Supabase Response: {response}")  # Debugging Output
    
    if response.data is None:
        return {"error": "No data returned. Check if RLS is blocking access or table name is incorrect."}
    
    return response.data  # Return actual data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
