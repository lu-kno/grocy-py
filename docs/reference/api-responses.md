# API Response Types

These are Pydantic `BaseModel` classes used to deserialize raw JSON responses from the Grocy API. They are used internally by `GrocyApiClient` and passed to the higher-level data model classes.

You typically don't construct these directly, but they document the shape of the API responses.

## Stock Responses

::: pygrocy.grocy_api_client.CurrentStockResponse

::: pygrocy.grocy_api_client.ProductDetailsResponse

::: pygrocy.grocy_api_client.MissingProductResponse

::: pygrocy.grocy_api_client.StockLogResponse

## Product Data

::: pygrocy.grocy_api_client.ProductData

::: pygrocy.grocy_api_client.ProductBarcodeData

::: pygrocy.grocy_api_client.QuantityUnitData

::: pygrocy.grocy_api_client.LocationData

## Chore Responses

::: pygrocy.grocy_api_client.CurrentChoreResponse

::: pygrocy.grocy_api_client.ChoreDetailsResponse

::: pygrocy.grocy_api_client.ChoreData

## Task Responses

::: pygrocy.grocy_api_client.TaskResponse

::: pygrocy.grocy_api_client.TaskCategoryDto

## Battery Responses

::: pygrocy.grocy_api_client.CurrentBatteryResponse

::: pygrocy.grocy_api_client.BatteryDetailsResponse

::: pygrocy.grocy_api_client.BatteryData

## Equipment Responses

::: pygrocy.grocy_api_client.EquipmentDetailsResponse

::: pygrocy.grocy_api_client.EquipmentData

## Meal Plan Responses

::: pygrocy.grocy_api_client.MealPlanResponse

::: pygrocy.grocy_api_client.MealPlanSectionResponse

::: pygrocy.grocy_api_client.RecipeDetailsResponse

## Shopping List

::: pygrocy.grocy_api_client.ShoppingListItem

## User

::: pygrocy.grocy_api_client.UserDto

## System

::: pygrocy.grocy_api_client.SystemInfoDto

::: pygrocy.grocy_api_client.SystemTimeDto

::: pygrocy.grocy_api_client.SystemConfigDto

::: pygrocy.grocy_api_client.GrocyVersionDto
