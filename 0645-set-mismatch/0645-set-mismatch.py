from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        duplicate = -1
        missing = 1
        
        # Check for duplicates and missing numbers
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
        
        # If the last number is not n, then the missing number must be n
        if nums[-1] != len(nums):
            missing = len(nums)
        
        res.append(duplicate)
        res.append(missing)
        
        return res
