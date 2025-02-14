import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    port = os.environ.get("PORT")  # Debugging PORT variable
    return {"message": f"FastAPI is running on PORT {port}"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Get PORT from Railway
    print(f"🚀 Running on PORT {port}")  # Debugging log
    uvicorn.run(app, host="0.0.0.0", port=port)

