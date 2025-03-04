from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = len(g)
        r = len(s)
        i = 0
        j = 0
        while i < r and j < l:
            if s[i] >= g[j]:
                j += 1
            i += 1  
        return j
