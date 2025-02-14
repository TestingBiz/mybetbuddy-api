import requests
from requests.auth import HTTPBasicAuth
import os
import uuid
from supabase import create_client

# Load API Keys
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
RACING_API_KEY = os.getenv("RACING_API_KEY")
RACING_API_SECRET = os.getenv("RACING_API_SECRET")

# Ensure Supabase credentials are set
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check environment variables.")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch race data
url = "https://api.theracingapi.com/v1/racecards/free"
response = requests.get(url, auth=HTTPBasicAuth(RACING_API_KEY, RACING_API_SECRET))
data = response.json()

# **FIXED: Ensure we use "racecards" instead of "races"**
if not isinstance(data, dict) or "racecards" not in data:
    raise ValueError(f"❌ Unexpected API response format: {data}")

# Insert races into Supabase
for race in data["racecards"]:  
    race_id = str(uuid.uuid4())  # Generate UUID for race
    race_data = {
        "id": race_id,
        "date": race.get("date", ""),
        "location": race.get("course", ""),  # "course" instead of "location"
    }
    print(f"Inserting into races: {race_data}")  # Debugging print statement

    response = supabase.table("races").insert(race_data).execute()
    print("Race insert response:", response)  # Print API response

    # Insert horses linked to this race
    for horse in race.get("runners", []):  
        horse_data = {
            "id": str(uuid.uuid4()),
            "race_id": race_id,
            "horse": horse.get("horse", ""),
            "trainer": horse.get("trainer", ""),
            "jockey": horse.get("jockey", ""),
            "owner": horse.get("owner", ""),
            "age": int(horse.get("age", 0)),
            "sex": horse.get("sex", ""),
            "weight": int(horse.get("lbs", 0)),
            "draw": int(horse.get("draw", 0)),
            "sire": horse.get("sire", ""),
            "dam": horse.get("dam", ""),
        }
        print(f"Inserting into horses: {horse_data}")  # Debugging print statement

        response = supabase.table("horses").insert(horse_data).execute()
        print("Horse insert response:", response)  # Print API response

print("✅ Data import attempt complete.")
