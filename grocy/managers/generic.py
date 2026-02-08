from __future__ import annotations

from typing import TYPE_CHECKING

from ..data_models.generic import EntityType

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class GenericEntityManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def list(
        self, entity_type: EntityType, query_filters: list[str] | None = None
    ) -> list[dict]:
        return (
            self._api.get_generic_objects_for_type(entity_type.value, query_filters)
            or []
        )

    def get(self, entity_type: EntityType, object_id: int) -> dict:
        return self._api.get_generic(entity_type.value, object_id)

    def create(self, entity_type: EntityType, data) -> dict:
        return self._api.add_generic(entity_type.value, data)

    def update(self, entity_type: EntityType, object_id: int, data):
        return self._api.update_generic(entity_type.value, object_id, data)

    def delete(self, entity_type: EntityType, object_id: int):
        return self._api.delete_generic(entity_type.value, object_id)

    def get_userfields(self, entity: str, object_id: int):
        return self._api.get_userfields(entity, object_id)

    def set_userfields(self, entity: str, object_id: int, key: str, value):
        return self._api.set_userfields(entity, object_id, key, value)
