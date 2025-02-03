class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i=1
        while(time>0):
            while(i<n and time>0):
                i+=1
                time-=1
            while(i>1 and time>0):
                i-=1
                time-=1
        return i
        