class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        count=0
       
        if n==1:
            return True
        elif n<=0:
            return False
       
        else:
            while n>1:
                if n%4==0:
                    count+=1
                    n//=4
                else:
                    return False
            return True
        
        