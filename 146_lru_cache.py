import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            element = self.cache.pop(key)
            self.cache[key] = element
            return element

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


# if __name__ == "__main__":
#     capacity = 3
#     obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
