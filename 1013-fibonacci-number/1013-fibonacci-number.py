class Solution:
    def fib(self, n: int) -> int:
        first=0
        second=1
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            for i in range(2,n+1):
                third=first+second
                first=second
                second=third
            return second

       
