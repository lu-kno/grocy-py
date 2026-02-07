# Errors

Exception classes raised by the library.

## GrocyError

Raised when the Grocy API returns an HTTP 4xx or 5xx response.

```python
from pygrocy2.errors import GrocyError

try:
    product = grocy.product(99999)
except GrocyError as e:
    print(f"HTTP {e.status_code}: {e.message}")
```

::: pygrocy2.errors.grocy_error.GrocyError
    options:
      members_order: source
