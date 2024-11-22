class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j = int(c**0.5)
        while i<=j:
            if i*i+j*j==c:
                return True
            elif i*i+j*j>c:
                j-=1
            else:
                i+=1
        return False

        