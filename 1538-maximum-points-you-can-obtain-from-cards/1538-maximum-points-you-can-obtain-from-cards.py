from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = 0
        max_sum = 0
        n = len(cardPoints) - 1
        right_sum = 0
        
        # Calculate the sum of the first k cards from the left
        for i in range(k):
            left_sum += cardPoints[i]
        max_sum = left_sum
        
        # Adjust by moving cards from the left end to the right end
        for i in range(k-1, -1, -1):
            left_sum -= cardPoints[i]       # Remove one card from the left sum
            right_sum += cardPoints[n]      # Add one card from the right sum
            max_sum = max(max_sum, left_sum + right_sum)
            n -= 1
        
        return max_sum


            


       