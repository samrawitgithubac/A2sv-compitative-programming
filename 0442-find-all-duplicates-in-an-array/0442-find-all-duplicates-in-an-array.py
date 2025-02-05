class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        res=[]
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                res.append(nums[i])
                i+=2
            else:
                i+=1
        return res
            


        