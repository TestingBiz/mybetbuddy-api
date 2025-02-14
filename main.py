from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway!"}

if __name__ == "__main__":
    import uvicorn
    port = 8000  # Hardcode the port instead of using os.getenv
    print(f"🚀 Running on port: {port}")  # Debugging log
    uvicorn.run(app, host="0.0.0.0", port=port)
