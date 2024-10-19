class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        n=min(len(word1),len(word2))
        s=""
        for i in range(n):
            s+=(word1[i])
            s+=(word2[i])
        s+= word1[l2:] if l1 > l2 else word2[l1:]
        return s





        