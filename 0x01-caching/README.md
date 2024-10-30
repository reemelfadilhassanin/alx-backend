# 0x01. Caching

## Back-end Project
*---

## Background Context

In this project, you will explore various caching algorithms. Caching is essential for optimizing system performance by temporarily storing frequently accessed data, which allows for quicker retrieval.

## Resources

To understand caching mechanisms better, review the following materials:

- [Cache Replacement Policies - FIFO](#)
- [Cache Replacement Policies - LIFO](#)
- [Cache Replacement Policies - LRU](#)
- [Cache Replacement Policies - MRU](#)
- [Cache Replacement Policies - LFU](#)

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- What a caching system is
- Definitions of FIFO, LIFO, LRU, MRU, and LFU
- The purpose and limitations of caching systems

## Requirements

### Python Scripts

- All files must be compatible with Python 3 (version 3.7) on Ubuntu 18.04 LTS.
- Each file should end with a new line.
- The first line of each file should be `#!/usr/bin/env python3`.
- A `README.md` file is mandatory at the root of the project folder.
- Code must adhere to the `pycodestyle` style (version 2.5).
- All files should be executable.
- The length of files will be verified using `wc`.
- Modules, classes, and functions must be properly documented.

### Documentation Requirements

- Each module should include a description of its purpose.
- Each class should provide an overview of its functionality.
- Each function should detail its purpose and parameters.

### Base Class: `BaseCaching`

All classes must inherit from `BaseCaching`, defined as follows:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines the constants of your caching system
        and where your data is stored (in a dictionary).
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache_data dictionary.
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the current cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item to the cache.

        Raises:
            NotImplementedError: If not implemented in the subclass.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Retrieve an item by key.

        Raises:
            NotImplementedError: If not implemented in the subclass.
        """
        raise NotImplementedError("get must be implemented in your cache class")
