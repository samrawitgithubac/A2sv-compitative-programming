class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        i=0
        for i in range(len(nums)):
            if nums[i]<k:
                count+=1
        return count
       
                
               

        