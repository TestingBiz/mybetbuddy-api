from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running on Railway!"}

if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.getenv("PORT", 8000))  # Use Railway's assigned port
    uvicorn.run(app, host="0.0.0.0", port=port)
