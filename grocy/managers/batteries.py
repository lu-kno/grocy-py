from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..data_models.battery import Battery

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class BatteryManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def list(
        self, query_filters: list[str] | None = None, get_details: bool = False
    ) -> list[Battery]:
        raw = self._api.get_batteries(query_filters)
        batteries = [Battery.from_current_response(bat) for bat in raw]
        if get_details:
            for item in batteries:
                item.get_details(self._api)
        return batteries

    def get(self, battery_id: int) -> Battery | None:
        battery = self._api.get_battery(battery_id)
        if battery:
            return Battery.from_details_response(battery)
        return None

    def charge(self, battery_id: int, tracked_time: datetime | None = None):
        return self._api.charge_battery(battery_id, tracked_time)

    def undo(self, charge_cycle_id: int):
        return self._api.undo_battery_charge(charge_cycle_id)
