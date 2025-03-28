class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-2]!=nums[n-1]:
            return nums[n-1]
        l=1
        r=len(nums)-2
        while l<=r:
            mid=(l+r)//2
            if (nums[mid-1]!=nums[mid]) and (nums[mid]!=nums[mid+1]):
                return nums[mid]
            if ((mid%2==1) and (nums[mid-1]==nums[mid])) or ((mid%2==0)and (nums[mid+1]==nums[mid])):
                l=mid+1
            else:
                r=mid-1
        return -1
        


        
        