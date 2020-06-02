# lib_hal9k

The **HackerLab 9000** controller library.

## Demo

```python
>>> from hal9k import Meta
>>> # Instantiate a Meta controller.
>>> meta = Meta()
>>> # Retrieve a track listing.
>>> meta.get_tracks()
['Debian 9.12 x64 (BASE)', 'Windows 8 x64 (BASE)', 'MSEdge - Win10 (BASE)', 'Debian 10.3 x64 (BASE)']
>>> # Instantiate a Track controller.
>>> track = meta.fetch('Debian 9.12 x64 (BASE)')
```

## Changelog

* **0.1.0** :: Added `Meta` class with `get_machines` function.
