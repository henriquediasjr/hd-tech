from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class ContactRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    message: str = Field(min_length=10, max_length=2000)


class ContactResponse(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    message: str
    status: str
