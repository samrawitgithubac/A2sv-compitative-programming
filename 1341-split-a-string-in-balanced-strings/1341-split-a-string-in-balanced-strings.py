class Solution:
    def balancedStringSplit(self, s: str) -> int:
        Rcount=Lcount=0
        i=0
        maxstring=0
        while i<len(s):
            if s[i]=='R':
                Rcount+=1
                i+=1
            else:
                Lcount+=1
                i+=1
            if Rcount==Lcount:
                maxstring+=1
        return  maxstring





        