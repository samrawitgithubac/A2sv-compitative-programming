from math import sqrt
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i = 0
        while i < k:
            s = max(gifts)
            w = int(sqrt(s))  # Ensure `w` is an integer after taking the square root
            l = gifts.index(s)
            gifts[l] = w
            i += 1
        return sum(gifts)  # Removed slicing as `sum(gifts[::len(gifts)])` is unnecessary
