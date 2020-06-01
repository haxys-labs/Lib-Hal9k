# lib_hal9k

The **HackerLab 9000** controller library.

## Installation Instructions



## Demo

Get a list of machines:

```python
>>> from hal9k import Meta
>>> meta = Meta()
>>> meta.get_machines()
['Debian 9.12 x64 (BASE)', 'Windows 8 x64 (BASE)', 'MSEdge - Win10 (BASE)', 'Debian 10.3 x64 (BASE)']
```

## Changelog

* **0.1.0** :: Added `Meta` class with `get_machines` function.
