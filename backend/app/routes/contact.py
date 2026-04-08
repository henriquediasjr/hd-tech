from fastapi import APIRouter, Depends
from app.schemas.contact import ContactRequest, ContactResponse
from app.repositories.base import BaseRepository
from app.repositories.contact_repo import get_contact_repository
from app.services.contact_service import handle_contact, list_contacts

router = APIRouter()


@router.post("/", response_model=ContactResponse, status_code=201)
def submit_contact(
    data: ContactRequest,
    repo: BaseRepository[ContactResponse] = Depends(get_contact_repository),
):
    return handle_contact(data, repo)


@router.get("/", response_model=list[ContactResponse])
def get_contacts(
    repo: BaseRepository[ContactResponse] = Depends(get_contact_repository),
):
    return list_contacts(repo)
