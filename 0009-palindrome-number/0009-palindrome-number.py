class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            reversenum=0
            a=x
            while a>0:
                id=a%10
                reversenum=reversenum*10+id
                a//=10
            if reversenum==x:
                return True
            else:
                return False
            
       
            



        