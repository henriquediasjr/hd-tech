from typing import Generic, TypeVar
from uuid import UUID

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """In-memory store. Swap internals for a DB session when PostgreSQL is wired."""

    def __init__(self) -> None:
        self._store: list[T] = []

    def save(self, entity: T) -> T:
        self._store.append(entity)
        return entity

    def list_all(self) -> list[T]:
        return list(self._store)

    def find_by_id(self, entity_id: UUID) -> T | None:
        return next((e for e in self._store if e.id == entity_id), None)  # type: ignore[attr-defined]
