from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_score = 0
        
        for _ in range(k):
            nums.sort()  # Sort the list in place
            max_value = nums[-1]  # Get the maximum value
            max_score += max_value  # Add it to the score
            nums[-1] += 1  # Increment the maximum value
            
        return max_score



        