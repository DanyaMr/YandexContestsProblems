from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.dct = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dct:
            self.dct.move_to_end(key=key)
            return self.dct[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            self.dct.move_to_end(key=key)
        else:
            if len(self.dct) == self.capacity:
                self.dct.popitem(last=False)
        self.dct[key] = value
