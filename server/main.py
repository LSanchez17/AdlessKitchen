from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import user_controller

app = FastAPI(title="AdlessKitchen - Server (dev)")

# CORS configuration
origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_controller.router)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get('/version')
async def version():
    # placeholder, update to return actual version from config or environment
    return {"version": "1.0.0"}

@app.get('/database')
async def database():
    # placeholder, update to check actual database connection
    return {"database": "connected"}