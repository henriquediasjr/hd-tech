from pydantic import BaseModel, Field, field_validator
from datetime import date
from enum import Enum
from uuid import UUID


class ProjectType(str, Enum):
    website = "website"
    ecommerce = "ecommerce"
    saas = "saas"
    mobile = "mobile"
    other = "other"


class BudgetRequest(BaseModel):
    project_type: ProjectType
    description: str = Field(min_length=20, max_length=1000)
    budget: float = Field(gt=0)
    deadline: date

    @field_validator("deadline")
    @classmethod
    def deadline_must_be_future(cls, v: date) -> date:
        if v <= date.today():
            raise ValueError("deadline must be a future date")
        return v


class BudgetResponse(BaseModel):
    id: UUID
    project_type: ProjectType
    description: str
    budget: float
    deadline: date
    message: str
