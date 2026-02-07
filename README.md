# pygrocy2
Check out [source code reference docs](https://iamkarlson.github.io/pygrocy2/)

## Installation

`pip install pygrocy2`

## Usage

Import the package:

```python
from pygrocy2 import Grocy
```

Obtain a grocy instance:

```python
grocy = Grocy("https://example.com", "GROCY_API_KEY")
```

or

```python
grocy = Grocy("https://example.com", "GROCY_API_KEY", port = 9192, verify_ssl = True)
```

Get current stock:

```python
for entry in grocy.stock():
    print("{} in stock for product id {}".format(entry.available_amount, entry.id))
```

# Support

If you need help using pygrocy check the [discussions](https://github.com/flipper/pygrocy2/issues) section. Feel free to create an issue for feature requests, bugs and errors in the library.

## Development testing

You need tox and Python 3.13 to run the tests. Navigate to the root dir of `pygrocy2` and execute `tox` to run the tests.
