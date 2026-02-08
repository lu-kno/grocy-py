from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class FileManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def upload(self, group: str, file_name: str, data):
        return self._api.upload_file(group, file_name, data)

    def download(self, group: str, file_name: str):
        return self._api.download_file(group, file_name)

    def delete(self, group: str, file_name: str):
        return self._api.delete_file(group, file_name)
