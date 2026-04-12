from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from typing import Optional


class ContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    need: Optional[str] = Field(default="", max_length=300)
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    need: Optional[str] = ""
    message: str
    status: str
