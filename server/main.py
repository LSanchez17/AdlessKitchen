from fastapi import FastAPI

app = FastAPI(title="AdlessKitchen - Server (dev)")

@app.get("/health")
async def health():
    return {"status": "ok"}