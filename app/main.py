from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}

@app.get("/ping")
def ping():
    return {"message": "pong"}