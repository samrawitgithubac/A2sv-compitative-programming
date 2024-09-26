class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        # Initialize the first three values
        t0, t1, t2 = 0, 1, 1
        
        # Iterate to calculate the nth Tribonacci number
        for i in range(3, n+1):
            t3 = t0 + t1 + t2  # Calculate the next number
            t0 = t1  # Move t0 to t1
            t1 = t2  # Move t1 to t2
            t2 = t3  # Move t2 to the new value
        
        return t2  # t2 will hold the nth Tribonacci number

        