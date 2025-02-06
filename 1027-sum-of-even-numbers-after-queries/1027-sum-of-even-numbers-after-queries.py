from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)  # Initial sum of even numbers
        answer = []

        for val, index in queries:
            if nums[index] % 2 == 0:  # If nums[index] was even, remove it from even_sum
                even_sum -= nums[index]

            nums[index] += val  # Apply the query update

            if nums[index] % 2 == 0:  # If the new nums[index] is even, add it to even_sum
                even_sum += nums[index]

            answer.append(even_sum)  # Store the updated even sum

        return answer
