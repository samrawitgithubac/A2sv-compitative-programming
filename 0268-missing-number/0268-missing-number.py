class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        totalnum=n*(n+1)//2
        sumss=sum(nums)
        return totalnum-sumss
        