from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        right = 0
        fruit_count = {}
        max_fruits = 0

        while right < len(fruits):
            # Add the current fruit to the basket
            if fruits[right] in fruit_count:
                fruit_count[fruits[right]] += 1
            else:
                fruit_count[fruits[right]] = 1

            # Check if we have more than 2 types of fruits
            while len(fruit_count) > 2:
                # Remove fruits from the left side
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            # Calculate the maximum fruits we can collect
            max_fruits = max(max_fruits, right - left + 1)
            right += 1

        return max_fruits


