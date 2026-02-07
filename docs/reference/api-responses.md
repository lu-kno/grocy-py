# API Response Types

These are Pydantic `BaseModel` classes used to deserialize raw JSON responses from the Grocy API. They are used internally by `GrocyApiClient` and passed to the higher-level data model classes.

You typically don't construct these directly, but they document the shape of the API responses.

## Stock Responses

::: pygrocy2.grocy_api_client.CurrentStockResponse

::: pygrocy2.grocy_api_client.ProductDetailsResponse

::: pygrocy2.grocy_api_client.MissingProductResponse

::: pygrocy2.grocy_api_client.StockLogResponse

## Product Data

::: pygrocy2.grocy_api_client.ProductData

::: pygrocy2.grocy_api_client.ProductBarcodeData

::: pygrocy2.grocy_api_client.QuantityUnitData

::: pygrocy2.grocy_api_client.LocationData

## Chore Responses

::: pygrocy2.grocy_api_client.CurrentChoreResponse

::: pygrocy2.grocy_api_client.ChoreDetailsResponse

::: pygrocy2.grocy_api_client.ChoreData

## Task Responses

::: pygrocy2.grocy_api_client.TaskResponse

::: pygrocy2.grocy_api_client.TaskCategoryDto

## Battery Responses

::: pygrocy2.grocy_api_client.CurrentBatteryResponse

::: pygrocy2.grocy_api_client.BatteryDetailsResponse

::: pygrocy2.grocy_api_client.BatteryData

## Equipment Responses

::: pygrocy2.grocy_api_client.EquipmentDetailsResponse

::: pygrocy2.grocy_api_client.EquipmentData

## Meal Plan Responses

::: pygrocy2.grocy_api_client.MealPlanResponse

::: pygrocy2.grocy_api_client.MealPlanSectionResponse

::: pygrocy2.grocy_api_client.RecipeDetailsResponse

## Shopping List

::: pygrocy2.grocy_api_client.ShoppingListItem

## User

::: pygrocy2.grocy_api_client.UserDto

## System

::: pygrocy2.grocy_api_client.SystemInfoDto

::: pygrocy2.grocy_api_client.SystemTimeDto

::: pygrocy2.grocy_api_client.SystemConfigDto

::: pygrocy2.grocy_api_client.GrocyVersionDto
