from fastapi import APIRouter
from app.routes import contact, schedule

api_router = APIRouter(prefix="/api")
api_router.include_router(contact.router, prefix="/contact", tags=["Contact"])
api_router.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])