from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..data_models.chore import Chore

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class ChoreManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def list(
        self, get_details: bool = False, query_filters: list[str] | None = None
    ) -> list[Chore]:
        raw_chores = self._api.get_chores(query_filters)
        chores = [Chore.from_current_response(chore) for chore in raw_chores]
        if get_details:
            for chore in chores:
                chore.get_details(self._api)
        return chores

    def get(self, chore_id: int) -> Chore:
        resp = self._api.get_chore(chore_id)
        return Chore.from_details_response(resp)

    def execute(
        self,
        chore_id: int,
        done_by: int | None = None,
        tracked_time: datetime | None = None,
        skipped: bool = False,
    ):
        return self._api.execute_chore(chore_id, done_by, tracked_time, skipped)

    def undo(self, execution_id: int):
        return self._api.undo_chore_execution(execution_id)

    def merge(self, chore_id_keep: int, chore_id_remove: int):
        return self._api.merge_chores(chore_id_keep, chore_id_remove)

    def calculate_next_assignments(self):
        return self._api.calculate_chore_assignments()
