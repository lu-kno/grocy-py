from __future__ import annotations

import base64
from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel


class RecipeItem(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    base_servings: int
    desired_servings: int
    picture_file_name: str | None = None

    @classmethod
    def from_response(cls, resp) -> RecipeItem:
        return cls(
            id=resp.id,
            name=resp.name,
            description=resp.description,
            base_servings=resp.base_servings,
            desired_servings=resp.desired_servings,
            picture_file_name=resp.picture_file_name,
        )

    def get_picture_url_path(self, width: int = 400):
        if self.picture_file_name:
            b64name = base64.b64encode(self.picture_file_name.encode("ascii"))
            path = "files/recipepictures/" + str(b64name, "utf-8")
            return f"{path}?force_serve_as=picture&best_fit_width={width}"


class MealPlanSection(BaseModel):
    id: int | None = None
    name: str | None = None
    sort_number: int | None = None
    row_created_timestamp: datetime | None = None

    @classmethod
    def from_response(cls, resp) -> MealPlanSection:
        return cls(
            id=resp.id,
            name=resp.name,
            sort_number=resp.sort_number,
            row_created_timestamp=resp.row_created_timestamp,
        )


class MealPlanItemType(str, Enum):
    NOTE = "note"
    PRODUCT = "product"
    RECIPE = "recipe"


class MealPlanItem(BaseModel):
    id: int
    day: date | None = None
    recipe_id: int | None = None
    recipe_servings: int | None = None
    note: str | None = None
    recipe: RecipeItem | None = None
    section_id: int | None = None
    section: MealPlanSection | None = None
    type: MealPlanItemType
    product_id: int | None = None

    @classmethod
    def from_response(cls, resp) -> MealPlanItem:
        day = cls._normalize_day(resp.day)
        return cls(
            id=resp.id,
            day=day,
            recipe_id=resp.recipe_id,
            recipe_servings=resp.recipe_servings,
            note=resp.note,
            section_id=resp.section_id,
            type=MealPlanItemType(resp.type),
            product_id=resp.product_id,
        )

    def get_details(self, api_client):
        if self.recipe_id:
            recipe = api_client.get_recipe(self.recipe_id)
            if recipe:
                self.recipe = RecipeItem.from_response(recipe)
        if self.section_id:
            section = api_client.get_meal_plan_section(self.section_id)
            if section:
                self.section = MealPlanSection.from_response(section)

    @staticmethod
    def _normalize_day(value) -> date | None:
        if value is None:
            return None
        if isinstance(value, date) and not isinstance(value, datetime):
            return value
        if isinstance(value, datetime):
            return value.date()
        return datetime.fromisoformat(str(value)).date()
