class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the first two steps
        first = 1
        second = 2
       
        # Iterate and calculate the number of ways for each step
        for i in range(3, n+1):
            third = first + second  # The current number of ways
            first = second  # Move the first pointer
            second = third  # Move the second pointer
       
        return second  # The final number of ways to reach step `n`

        