# Caching

 
# Cache Implementations

This repository contains implementations of various cache types done for alx-backend project, including First-In-First-Out (FIFO) Cache, Last-In-First-Out (LIFO) Cache, Least Recently Used (LRU) Cache, Most Recently Used (MRU) Cache, and Least Frequently Used (LFU) Cache. These cache implementations are designed to improve performance by efficiently managing and retrieving cached data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Cache Implementations](#cache-implementations)
  - [FIFO Cache](#fifo-cache)
  - [LIFO Cache](#lifo-cache)
  - [LRU Cache](#lru-cache)
  - [MRU Cache](#mru-cache)
  - [LFU Cache](#lfu-cache)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Caching is a common technique used in computer systems to store frequently accessed data in a fast-access memory, thereby reducing the time and resources required to retrieve the data from slower storage systems. This repository provides optimized implementations of various cache replacement policies: FIFO, LIFO, LRU, MRU, and LFU. These cache implementations are based on the principles of efficient data management and retrieval.

## Features

- Optimized implementations of FIFO, LIFO, LRU, MRU, and LFU caches
- Efficient cache replacement policies for improved performance
- Easy integration into Python projects
- Well-structured and documented code
- Simple and intuitive API for cache management

## Installation

To use the optimized cache implementations in your Python projects, follow these steps:

1. Clone the repository:

```shell
$ git clone https://github.com/TgGeda/alx-backend.git
```

2. Change into the project directory:

```
$ cd alx-backend/0x01-caching
```

3. Install the required dependencies:

```
$ pip install -r requirements.txt
```

## Usage

To utilize the optimized cache implementations in your Python projects, follow these steps:

1. Import the desired cache class:

```
from 0x01-caching import FIFOCache, LIFOCache, LRUCache, MRUCache, LFUCache
```

2. Create an instance of the cache class:

```
cache = FIFOCache()  # or LIFOCache(), LRUCache(), MRUCache(), LFUCache()
```

3. Use the cache by calling the `put` and `get` methods:

```
cache.put(key, value)
cached_value = cache.get(key)
```

4. Adjust the cache size (if needed):

By default, the maximum number of items in the cache is set to a value defined in each cache class. You can modify this value by passing the `max_size` parameter to the cache constructor.

## Cache Implementations

### FIFO Cache

The First-In-First-Out (FIFO) Cache implementation provides a caching system where the items are evicted in the same order they were added to the cache. This strategy ensures that the oldest items are removed first when the cache reaches its maximum capacity.

The `1-fifo_cache.py` file contains the optimized implementation of the FIFO Cache.

### LIFO Cache

The Last-In-First-Out (LIFO) Cache implementation provides a caching system where the most recently added items are the first ones to be evicted. This strategy ensures that the newest items are removed first when the cache reaches its maximum capacity.

The `2-lifo_cache.py` file contains the optimized implementation of the LIFO Cache.

### LRU Cache

The Least Recently Used (LRU) Cache implementation provides a caching system where the least recently used items are evicted from the cache when it reaches its maximum capacity. This strategy ensures that the items that have been accessed least recently are removed first.

The `3-lru_cache.py` file contains the optimized implementation of the LRU Cache.

### MRU Cache

The Most Recently Used (MRU) Cache implementation provides a caching system where the most recently used items are kept in the cache, and when the cache is full, the least recently used item is evicted. This strategy is useful when there is a high chance of recently accessed items being accessed again soon.

The `4-mru_cache.py` file contains the optimized implementation of the MRU Cache.

### LFU Cache

The Least Frequently Used (LFU) Cache implementation provides a caching system where the least frequently accessed items are evicted from the cache when it reaches its maximum capacity. This strategy is useful when there is a need to prioritize items that are frequently accessed.

The `100-lfu_cache.py` file contains the optimized implementation of the LFU Cache.

## Contributing

Contributions to this repository are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. When contributing, please follow the existing code style and conventions and provide detailed information about the changes made.

## License

This repository is licensed under the [MIT License](LICENSE).
```

Feel free to customize this README file further to suit your specific requirements. Make sure to update the installation instructions and other relevant sections based on the actual steps required to install and use the optimized cache implementations.