from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value  # Move to end (most recently used)
        return value
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used
        self.cache[key] = value

# Test the cache
cache = LRUCache(2)
cache.put(1, 1)  # Cache: {1: 1}
cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(cache.get(1))  # Returns 1
cache.put(3, 3)  # Evicts key 2, Cache: {1: 1, 3: 3}
print(cache.get(2))  # Returns -1 (not found)