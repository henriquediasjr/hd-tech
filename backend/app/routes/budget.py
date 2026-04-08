from fastapi import APIRouter, Depends
from app.schemas.budget import BudgetRequest, BudgetResponse
from app.repositories.base import BaseRepository
from app.repositories.budget_repo import get_budget_repository
from app.services.budget_service import handle_budget, list_budgets

router = APIRouter()


@router.post("/", response_model=BudgetResponse, status_code=201)
def submit_budget(
    data: BudgetRequest,
    repo: BaseRepository[BudgetResponse] = Depends(get_budget_repository),
):
    return handle_budget(data, repo)


@router.get("/", response_model=list[BudgetResponse])
def get_budgets(
    repo: BaseRepository[BudgetResponse] = Depends(get_budget_repository),
):
    return list_budgets(repo)
