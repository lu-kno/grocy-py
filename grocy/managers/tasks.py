from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from ..data_models.task import Task

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class TaskManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def list(self, query_filters: list[str] | None = None) -> list[Task]:
        raw_tasks = self._api.get_tasks(query_filters)
        return [Task.from_response(task) for task in raw_tasks]

    def get(self, task_id: int) -> Task:
        resp = self._api.get_task(task_id)
        return Task.from_response(resp)

    def complete(self, task_id: int, done_time: datetime | None = None):
        return self._api.complete_task(task_id, done_time)

    def undo(self, task_id: int):
        return self._api.undo_task(task_id)
