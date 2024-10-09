class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        difference = 0
        for char in set(s):
            index_s = s.index(char)
            index_t = t.index(char)
            difference += abs(index_s - index_t)
        return difference
        