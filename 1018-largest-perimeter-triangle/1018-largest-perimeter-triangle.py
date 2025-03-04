class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i=2
        while i<len(nums):
            if nums[i]+nums[i-1]>nums[i-2]:
                return nums[i-1]+nums[i-2]+nums[i] 
            i+=1
            
        return 0
               
        
            