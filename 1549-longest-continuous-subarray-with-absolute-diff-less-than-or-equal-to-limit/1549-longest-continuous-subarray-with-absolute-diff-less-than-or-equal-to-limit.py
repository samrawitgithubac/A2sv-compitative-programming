class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dec=deque()
        inc=deque()
        l=0
        ans=float("-inf")
        for r in range(len(nums)):
            while dec and dec[-1]<nums[r]:
                dec.pop()
            dec.append(nums[r])
            while inc and inc[-1]>nums[r]:
                inc.pop()
            inc.append(nums[r])
            # mini,maxi=inc[0],dec[0]
            while dec[0]-inc[0]>limit:
                val=nums[l]
                if inc[0]==val:
                    inc.popleft()
                if dec[0]==val:
                    dec.popleft()
                l+=1
            ans =max(ans,r-l+1)
        return ans
