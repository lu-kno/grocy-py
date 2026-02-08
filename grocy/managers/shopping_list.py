from __future__ import annotations

from typing import TYPE_CHECKING

from ..data_models.product import ShoppingListProduct

if TYPE_CHECKING:
    from ..grocy_api_client import GrocyApiClient


class ShoppingListManager:
    def __init__(self, api_client: GrocyApiClient):
        self._api = api_client

    def items(
        self, get_details: bool = False, query_filters: list[str] | None = None
    ) -> list[ShoppingListProduct]:
        raw = self._api.get_shopping_list(query_filters)
        shopping_list = [
            ShoppingListProduct.from_shopping_list_item(item) for item in raw
        ]
        if get_details:
            for item in shopping_list:
                item.get_details(self._api)
        return shopping_list

    def add_product(
        self,
        product_id: int,
        shopping_list_id: int | None = None,
        amount: float | None = None,
        quantity_unit_id: int | None = None,
    ):
        return self._api.add_product_to_shopping_list(
            product_id, shopping_list_id, amount, quantity_unit_id
        )

    def remove_product(
        self, product_id: int, shopping_list_id: int = 1, amount: float = 1
    ):
        return self._api.remove_product_in_shopping_list(
            product_id, shopping_list_id, amount
        )

    def clear(self, shopping_list_id: int = 1):
        return self._api.clear_shopping_list(shopping_list_id)

    def add_missing_products(self, shopping_list_id: int = 1):
        return self._api.add_missing_product_to_shopping_list(shopping_list_id)

    def add_overdue_products(self, shopping_list_id: int = 1):
        return self._api.add_overdue_products_to_shopping_list(shopping_list_id)

    def add_expired_products(self, shopping_list_id: int = 1):
        return self._api.add_expired_products_to_shopping_list(shopping_list_id)
