import logging
from functools import cached_property

from .grocy_api_client import DEFAULT_PORT_NUMBER, GrocyApiClient
from .managers.batteries import BatteryManager
from .managers.calendar import CalendarManager
from .managers.chores import ChoreManager
from .managers.equipment import EquipmentManager
from .managers.files import FileManager
from .managers.generic import GenericEntityManager
from .managers.meal_plan import MealPlanManager
from .managers.recipes import RecipeManager
from .managers.shopping_list import ShoppingListManager
from .managers.stock import StockManager
from .managers.system import SystemManager
from .managers.tasks import TaskManager
from .managers.users import UserManager

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


class Grocy:
    def __init__(
        self,
        base_url,
        api_key,
        port: int = DEFAULT_PORT_NUMBER,
        path: str | None = None,
        verify_ssl=True,
        debug=False,
    ):
        self._api_client = GrocyApiClient(
            base_url, api_key, port, path, verify_ssl, debug
        )

        if debug:
            _LOGGER.setLevel(logging.DEBUG)

    @cached_property
    def stock(self) -> StockManager:
        return StockManager(self._api_client)

    @cached_property
    def shopping_list(self) -> ShoppingListManager:
        return ShoppingListManager(self._api_client)

    @cached_property
    def recipes(self) -> RecipeManager:
        return RecipeManager(self._api_client)

    @cached_property
    def chores(self) -> ChoreManager:
        return ChoreManager(self._api_client)

    @cached_property
    def tasks(self) -> TaskManager:
        return TaskManager(self._api_client)

    @cached_property
    def batteries(self) -> BatteryManager:
        return BatteryManager(self._api_client)

    @cached_property
    def equipment(self) -> EquipmentManager:
        return EquipmentManager(self._api_client)

    @cached_property
    def meal_plan(self) -> MealPlanManager:
        return MealPlanManager(self._api_client)

    @cached_property
    def users(self) -> UserManager:
        return UserManager(self._api_client)

    @cached_property
    def system(self) -> SystemManager:
        return SystemManager(self._api_client)

    @cached_property
    def generic(self) -> GenericEntityManager:
        return GenericEntityManager(self._api_client)

    @cached_property
    def calendar(self) -> CalendarManager:
        return CalendarManager(self._api_client)

    @cached_property
    def files(self) -> FileManager:
        return FileManager(self._api_client)
