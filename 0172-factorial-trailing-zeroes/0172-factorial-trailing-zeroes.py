class Solution:
    def trailingZeroes(self, n: int) -> int:
        # calculate the factorial of n
        def factorial(n):
            if n<2:
                return 1 
            return n*factorial(n-1)
        
        # counting the trailing zeroes
        fact_n=factorial(n)
        count=0
        while fact_n%10==0:
            count+=1
            fact_n=fact_n//10
        return count
