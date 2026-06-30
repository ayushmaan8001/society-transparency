from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from app.api.v1.endpoints import auth, societies, flats

security = HTTPBearer()

app = FastAPI(
    title="Society Transparency Management System",
    description="A resident-first platform for transparent society management",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(societies.router, prefix="/api/v1/societies", tags=["Societies"])
app.include_router(flats.router, prefix="/api/v1/societies/{society_id}/flats", tags=["Flats"])


@app.get("/")
def root():
    return {"message": "Society Transparency Management System is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}