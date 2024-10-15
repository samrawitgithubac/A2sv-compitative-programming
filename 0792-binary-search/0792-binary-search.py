from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search assumes the array is already sorted
        top = len(nums) - 1
        bottom = 0

        while bottom <= top:
            mid = (top + bottom) // 2

            if nums[mid] == target:
                return mid  # Return the index where the target is found
            elif nums[mid] < target:
                bottom = mid + 1  # Move to the right half
            else:
                top = mid - 1  # Move to the left half

        return -1  # Target not found
