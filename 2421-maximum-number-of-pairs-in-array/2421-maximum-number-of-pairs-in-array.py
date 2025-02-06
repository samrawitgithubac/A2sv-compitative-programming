from typing import List

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        count = 0  # Ensure count is initialized

        i = 1  # Initialize i properly
        while i < len(nums):  # Use while to avoid index skipping
            if nums[i - 1] == nums[i]:
                nums.pop(i)#del nums[i]  # Remove the current element
                nums.pop(i-1)#del nums[i - 1]  # Remove the previous element
                count += 1  # Increase pair count
            else:
                i += 1  # Move to the next index
        
        return [count, len(nums)]
