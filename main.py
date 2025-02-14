from fastapi import FastAPI
import os
from supabase import create_client
import json  # Import json to handle response conversion

# ✅ Load Supabase credentials from environment variables
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# ✅ Ensure credentials exist
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials! Check Railway environment variables.")

# ✅ Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ✅ Initialize FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway with Supabase!"}

@app.get("/races")
def get_races():
    """Fetch all races from Supabase."""
    response = supabase.table("races").select("*").execute()  # ✅ Ensure lowercase "races"

    # ✅ Debugging: Print the response to logs
    print("DEBUG: Supabase Response:", response.data)

    # ✅ Convert response to JSON format explicitly
    return json.loads(json.dumps(response.data))  

# ✅ Run the FastAPI app with Uvicorn if executed directly
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Use PORT from env or default to 8000
    uvicorn.run(app, host="0.0.0.0", port=port)
