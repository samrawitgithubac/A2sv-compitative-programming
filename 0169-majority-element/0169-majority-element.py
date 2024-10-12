from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # Return the element at the middle index
        return nums[len(nums) // 2]



        