from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class ProductBarcode(BaseModel):
    barcode: str
    amount: float | None = None


class QuantityUnit(BaseModel):
    id: int
    name: str
    name_plural: str | None = None
    description: str | None = None


class Product(BaseModel):
    id: int
    name: str | None = None
    product_group_id: int | None = None
    available_amount: float | None = None
    amount_aggregated: float | None = None
    amount_opened: float | None = None
    amount_opened_aggregated: float | None = None
    is_aggregated_amount: bool | None = None
    best_before_date: datetime | None = None
    barcodes: list[str] = []
    product_barcodes: list[ProductBarcode] = []
    amount_missing: float | None = None
    is_partly_in_stock: bool | None = None
    default_quantity_unit_purchase: QuantityUnit | None = None

    @classmethod
    def from_stock_response(cls, resp) -> Product:
        barcodes_list: list[ProductBarcode] = []
        name = None
        product_group_id = None
        if resp.product:
            name = resp.product.name
            product_group_id = resp.product.product_group_id
        return cls(
            id=resp.product_id,
            name=name,
            product_group_id=product_group_id,
            available_amount=resp.amount,
            amount_aggregated=resp.amount_aggregated,
            amount_opened=resp.amount_opened,
            amount_opened_aggregated=resp.amount_opened_aggregated,
            is_aggregated_amount=resp.is_aggregated_amount,
            best_before_date=resp.best_before_date,
            product_barcodes=barcodes_list,
            barcodes=[],
        )

    @classmethod
    def from_missing_response(cls, resp) -> Product:
        return cls(
            id=resp.id,
            name=resp.name,
            amount_missing=resp.amount_missing,
            is_partly_in_stock=resp.is_partly_in_stock,
        )

    @classmethod
    def from_details_response(cls, resp) -> Product:
        product_barcodes = (
            [ProductBarcode(barcode=b.barcode, amount=b.amount) for b in resp.barcodes]
            if resp.barcodes
            else []
        )
        barcodes = [b.barcode for b in product_barcodes]
        name = None
        product_group_id = None
        product_id = 0
        if resp.product:
            product_id = resp.product.id
            name = resp.product.name
            product_group_id = resp.product.product_group_id
        qu = None
        if resp.default_quantity_unit_purchase:
            qu = QuantityUnit(
                id=resp.default_quantity_unit_purchase.id,
                name=resp.default_quantity_unit_purchase.name,
                name_plural=resp.default_quantity_unit_purchase.name_plural,
                description=resp.default_quantity_unit_purchase.description,
            )
        return cls(
            id=product_id,
            name=name,
            product_group_id=product_group_id,
            available_amount=resp.stock_amount,
            best_before_date=resp.next_best_before_date,
            product_barcodes=product_barcodes,
            barcodes=barcodes,
            default_quantity_unit_purchase=qu,
        )

    @classmethod
    def from_product_data(cls, data) -> Product:
        return cls(
            id=data.id,
            name=data.name,
            product_group_id=data.product_group_id,
        )

    @classmethod
    def from_stock_log_response(cls, resp) -> Product:
        return cls(id=resp.product_id)

    def get_details(self, api_client):
        details = api_client.get_product(self.id)
        if details:
            updated = Product.from_details_response(details)
            # Preserve fields that the details response doesn't provide
            preserved = {}
            for field in ("amount_missing", "is_partly_in_stock"):
                current = getattr(self, field, None)
                if current is not None:
                    preserved[field] = current
            self.__dict__.update(updated.__dict__)
            for field, value in preserved.items():
                setattr(self, field, value)


class Group(BaseModel):
    id: int
    name: str
    description: str | None = None


class ShoppingListProduct(BaseModel):
    id: int
    product_id: int | None = None
    amount: float | None = None
    note: str | None = None
    product: Product | None = None
    done: bool = False

    @classmethod
    def from_shopping_list_item(cls, item) -> ShoppingListProduct:
        return cls(
            id=item.id,
            product_id=item.product_id,
            note=item.note,
            amount=item.amount,
            done=bool(item.done),
        )

    def get_details(self, api_client):
        if self.product_id:
            resp = api_client.get_product(self.product_id)
            if resp:
                self.product = Product.from_details_response(resp)
