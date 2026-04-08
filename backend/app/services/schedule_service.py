from app.core.config import settings


def get_schedule_info() -> dict:
    return {
        "calendly_url": settings.CALENDLY_URL,
        "message": "Pick a time that works best for you.",
    }
