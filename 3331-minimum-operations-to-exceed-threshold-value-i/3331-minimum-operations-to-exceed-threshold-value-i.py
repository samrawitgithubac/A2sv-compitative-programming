class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        i=0
        while i<len(nums):
            if nums[i]<k:
                nums.remove(nums[i])
                count+=1
            else:
                i+=1
        return count
                
               

        