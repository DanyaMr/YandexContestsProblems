import random


class RandomizedSet:

    def __init__(self):
        self.nums_dict = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        if val in self.nums_dict:
            return False

        self.nums_dict[val] = len(self.nums_list)
        self.nums_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_list:
            return False
        
        id_to_remove = self.nums_dict[val]
        last_element = self.nums_list[-1]

        self.nums_list[id_to_remove] = last_element
        self.nums_dict[last_element] = id_to_remove
        
        self.nums_list.pop()
        del self.nums_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums_list)
