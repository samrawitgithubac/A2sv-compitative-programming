class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = list(set(nums))
        b = sorted(a)
        if len(b) < 3:
            return b[-1]
        else:
            return b[-3]