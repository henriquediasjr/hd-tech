from fastapi import APIRouter
from app.routes import contact, budget, schedule

api_router = APIRouter(prefix="/api")
api_router.include_router(contact.router, prefix="/contact", tags=["Contact"])
api_router.include_router(budget.router, prefix="/budget", tags=["Budget"])
api_router.include_router(schedule.router, prefix="/schedule", tags=["Schedule"])