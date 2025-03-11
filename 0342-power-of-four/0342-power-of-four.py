class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n<=0:
            return False
        else:
            a=math.log(n)/math.log(4)
            return (a==int(a))

        

        
        
    