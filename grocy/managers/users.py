from __future__ import annotations

from typing import TYPE_CHECKING

from ..data_models.user import User

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class UserManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def list(self) -> list[User]:
        user_dtos = self._api.get_users()
        return [
            User(
                id=u.id,
                username=u.username,
                first_name=u.first_name,
                last_name=u.last_name,
                display_name=u.display_name,
            )
            for u in user_dtos
        ]

    def get(self, user_id: int) -> User | None:
        user = self._api.get_user(user_id=user_id)
        if user:
            return User(
                id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                display_name=user.display_name,
            )
        return None

    def current(self) -> User | None:
        user = self._api.get_current_user()
        if user:
            return User(
                id=user.id,
                username=user.username,
                first_name=user.first_name,
                last_name=user.last_name,
                display_name=user.display_name,
            )
        return None

    def create(self, data: dict):
        return self._api.create_user(data)

    def edit(self, user_id: int, data: dict):
        return self._api.edit_user(user_id, data)

    def delete(self, user_id: int):
        return self._api.delete_user(user_id)

    def settings(self):
        return self._api.get_user_settings()

    def get_setting(self, key: str):
        return self._api.get_user_setting(key)

    def set_setting(self, key: str, value):
        return self._api.set_user_setting(key, value)

    def delete_setting(self, key: str):
        return self._api.delete_user_setting(key)
