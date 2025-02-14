import os
import uuid
import requests
from supabase import create_client
from requests.auth import HTTPBasicAuth

# Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("❌ Missing Supabase credentials! Check Railway environment variables.")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Racing API credentials
API_KEY = "YOUR_RACING_API_KEY"
API_SECRET = "YOUR_RACING_API_SECRET"

url = "https://api.theracingapi.com/v1/racecards/free"
response = requests.get(url, auth=HTTPBasicAuth(API_KEY, API_SECRET))

if response.status_code != 200:
    raise ValueError(f"❌ API Error: {response.json()}")

racecards = response.json().get("racecards", [])

for race in racecards:
    race_id = str(uuid.uuid4())  # Generate a unique race ID
    race_data = {
        "id": race_id,
        "date": race["date"],
        "location": race["location"]
    }

    # Insert into races table
    supabase.table("races").insert(race_data).execute()

    # Insert horses into horses table
    horses = race.get("horses", [])
    for horse in horses:
        horse_data = {
            "id": str(uuid.uuid4()),
            "race_id": race_id,  # Foreign key to races table
            "horse_name": horse["horse"],
            "age": horse["age"],
            "sex": horse["sex"],
            "trainer": horse["trainer"],
            "jockey": horse["jockey"],
            "weight": horse["lbs"],
            "headgear": horse["headgear"],
            "draw": horse["draw"],
            "form": horse["form"],
            "owner": horse["owner"],
            "sire": horse["sire"],
            "dam": horse["dam"]
        }
        supabase.table("horses").insert(horse_data).execute()

print("✅ Data inserted successfully into races and horses tables!")

