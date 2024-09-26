from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the result array with 1s
        result = [1] * n

        # First pass: Calculate the left product (prefix product)
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: Calculate the right product (suffix product) and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result
