from collections import  Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        S_Counter=Counter(s)
        res=[]
        for i in S_Counter:
            res.append(S_Counter[i])
        resset=set(res)
        if len(resset)==1:
            return True
        else:
            return False

        