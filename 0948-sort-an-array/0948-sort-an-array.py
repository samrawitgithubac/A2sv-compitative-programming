from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2
                leftnums = nums[:mid]
                rightnums = nums[mid:]

                # Recursively sort both halves
                mergeSort(leftnums)
                mergeSort(rightnums)

                i = j = k = 0

                # Merge sorted halves
                while i < len(leftnums) and j < len(rightnums):
                    if leftnums[i] < rightnums[j]:
                        nums[k] = leftnums[i]
                        i += 1
                    else:
                        nums[k] = rightnums[j]
                        j += 1
                    k += 1

                # Copy remaining elements from left half
                while i < len(leftnums):
                    nums[k] = leftnums[i]
                    i += 1
                    k += 1

                # Copy remaining elements from right half
                while j < len(rightnums):
                    nums[k] = rightnums[j]
                    j += 1
                    k += 1

        # Call merge sort
        mergeSort(nums)
        return nums

# Example usage:
solution = Solution()
arr = [38, 27, 43, 3, 9, 82, 10]
print(solution.sortArray(arr))  
# Output: [3, 9, 10, 27, 38, 43, 82]
