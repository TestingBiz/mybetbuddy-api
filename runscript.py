import requests
from requests.auth import HTTPBasicAuth
import os

RACING_API_KEY = os.getenv("RACING_API_KEY")
RACING_API_SECRET = os.getenv("RACING_API_SECRET")

url = "https://api.theracingapi.com/v1/racecards/free"
response = requests.get(url, auth=HTTPBasicAuth(RACING_API_KEY, RACING_API_SECRET))

data = response.json()
print(data)  # Inspect the full response format

