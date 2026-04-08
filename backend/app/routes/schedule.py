from fastapi import APIRouter
from app.schemas.schedule import ScheduleResponse
from app.services.schedule_service import get_schedule_info

router = APIRouter()


@router.get("/", response_model=ScheduleResponse)
def get_schedule():
    return get_schedule_info()
