from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DevOps monitoring project is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}