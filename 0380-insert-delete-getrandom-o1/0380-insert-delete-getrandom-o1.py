import random  # Importing random module for randint

class RandomizedSet:

    def __init__(self):
        self.index_map = {}          # Maps values to their indices in the list
        self.lists_elements = []     # Stores the actual elements

    def insert(self, val: int) -> bool:
        if val not in self.index_map:                # Corrected variable name (val instead of value)
            self.index_map[val] = len(self.lists_elements)
            self.lists_elements.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            remove_index = self.index_map[val]
            last_element = self.lists_elements[-1]

            # Swap the element to remove with the last element
            self.lists_elements[remove_index], self.lists_elements[-1] = last_element, val
            self.index_map[last_element] = remove_index

            # Remove the last element
            self.lists_elements.pop()
            del self.index_map[val]                 # Corrected indentation

            return True
        return False

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.lists_elements) - 1)  # Fixed typo and import
        return self.lists_elements[random_index]                       # Corrected return statement


# Test Example:
# obj = RandomizedSet()
# print(obj.insert(10))   # True
# print(obj.insert(20))   # True
# print(obj.remove(10))   # True
# print(obj.getRandom())  # 20 (since only 20 is left)
