from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                # Compare concatenated values as strings to determine order
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # Handle the edge case where all numbers are zero
        if nums[0] == 0:
            return "0"
        
        # Convert the sorted numbers to a single concatenated string
        return "".join(map(str, nums))
