class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            if not any(l <= i <= r for l, r in ranges):
                return False
        return True