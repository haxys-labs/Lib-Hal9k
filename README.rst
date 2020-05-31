lib_hal9k
=========

The **HackerLab 9000** controller library.

Demo
----
Get a list of machines:

.. code_block:: python

    >>> from hal9k.meta import Meta
    >>> meta = Meta()
    >>> meta.get_machines()
    ['Debian 9.12 x64 (BASE)', 'Windows 8 x64 (BASE)', 'MSEdge - Win10 (BASE)', 'Debian 10.3 x64 (BASE)']
