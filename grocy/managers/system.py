from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..data_models.system import SystemConfig, SystemInfo, SystemTime

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class SystemManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def info(self) -> SystemInfo | None:
        raw = self._api.get_system_info()
        if raw:
            return SystemInfo.from_dto(raw)
        return None

    def time(self) -> SystemTime | None:
        raw = self._api.get_system_time()
        if raw:
            return SystemTime.from_dto(raw)
        return None

    def config(self) -> SystemConfig | None:
        raw = self._api.get_system_config()
        if raw:
            return SystemConfig.from_dto(raw)
        return None

    def db_changed_time(self) -> datetime | None:
        return self._api.get_last_db_changed()
