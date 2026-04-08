from app.repositories.base import BaseRepository
from app.schemas.contact import ContactResponse

_contact_repository = BaseRepository[ContactResponse]()


def get_contact_repository() -> BaseRepository[ContactResponse]:
    return _contact_repository
