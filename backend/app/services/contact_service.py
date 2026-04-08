from uuid import uuid4
from app.core.logging import get_logger
from app.repositories.base import BaseRepository
from app.schemas.contact import ContactRequest, ContactResponse

logger = get_logger(__name__)


def handle_contact(
    data: ContactRequest,
    repo: BaseRepository[ContactResponse],
) -> ContactResponse:
    entry = ContactResponse(
        id=uuid4(),
        name=data.name,
        email=data.email,
        message=data.message,
        status="received",
    )
    repo.save(entry)
    logger.info("Contact received | id=%s email=%s", entry.id, entry.email)
    return entry


def list_contacts(repo: BaseRepository[ContactResponse]) -> list[ContactResponse]:
    return repo.list_all()
