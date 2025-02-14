from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Get PORT from env, default to 8000
    print(f"Starting server on port {port}...")  # Debugging output
    uvicorn.run(app, host="0.0.0.0", port=port)
