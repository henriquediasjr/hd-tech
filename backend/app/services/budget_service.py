from uuid import uuid4
from app.core.logging import get_logger
from app.repositories.base import BaseRepository
from app.schemas.budget import BudgetRequest, BudgetResponse

logger = get_logger(__name__)


def handle_budget(
    data: BudgetRequest,
    repo: BaseRepository[BudgetResponse],
) -> BudgetResponse:
    entry = BudgetResponse(
        id=uuid4(),
        project_type=data.project_type,
        description=data.description,
        budget=data.budget,
        deadline=data.deadline,
        message="Budget request received. We'll review and contact you shortly.",
    )
    repo.save(entry)
    logger.info("Budget received | id=%s type=%s budget=%.2f", entry.id, entry.project_type, entry.budget)
    return entry


def list_budgets(repo: BaseRepository[BudgetResponse]) -> list[BudgetResponse]:
    return repo.list_all()
