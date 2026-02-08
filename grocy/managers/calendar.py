from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class CalendarManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def ical(self) -> str | None:
        return self._api.get_calendar_ical()

    def sharing_link(self) -> str | None:
        return self._api.get_calendar_sharing_link()
