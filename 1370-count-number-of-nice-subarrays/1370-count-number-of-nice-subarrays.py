class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result, cur, l, cur_sub = 0, 0, 0, 0
        for r, v in enumerate(nums):
            if v % 2 == 1: 
                cur += 1
                cur_sub = 0

            while cur == k:
                if nums[l] % 2 == 1:
                    cur -= 1
                l += 1
                cur_sub += 1
            result += cur_sub

        return result
        