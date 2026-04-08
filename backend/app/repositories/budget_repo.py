from app.repositories.base import BaseRepository
from app.schemas.budget import BudgetResponse

_budget_repository = BaseRepository[BudgetResponse]()


def get_budget_repository() -> BaseRepository[BudgetResponse]:
    return _budget_repository
