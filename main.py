from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if Railway doesn't provide a port
    uvicorn.run(app, host="0.0.0.0", port=port)



