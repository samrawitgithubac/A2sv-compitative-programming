class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        ans=float('inf')
        while left<=right:
            mid=(left+right)//2
            if nums[left]<=nums[mid]:
                ans=min(ans,nums[left])
                left=mid+1
               
            else:
                ans=min(ans,nums[mid])
                right=mid-1
        return ans
                


        