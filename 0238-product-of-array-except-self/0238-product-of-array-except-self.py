from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize the answer array where answer[i] is the product of all elements except nums[i]
        answer = [1] * n
        
        # First pass: Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix  # Store the prefix product in answer[i]
            prefix *= nums[i]   # Update the prefix product to include nums[i]

        # Second pass: Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix  # Multiply the current suffix with the already stored prefix
            suffix *= nums[i]    # Update the suffix product to include nums[i]

        return answer
