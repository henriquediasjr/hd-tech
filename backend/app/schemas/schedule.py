from pydantic import BaseModel, HttpUrl


class ScheduleResponse(BaseModel):
    calendly_url: str
    message: str
