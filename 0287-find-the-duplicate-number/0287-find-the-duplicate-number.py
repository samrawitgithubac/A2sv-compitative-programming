class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
         nums.sort()
         i=0
         while i<len(nums):
            if nums[i]==nums[i+1]:
                return nums[i]
            i+=1
         
     


        