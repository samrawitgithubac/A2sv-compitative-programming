class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # See Merge Sort and 493. Reverse Pairs before this
        # This problem is exactly as 493, but we need to transform the two input
        # arrays to one first
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff, can be written as
        # nums1[i] - nums2[i] <= nums1[j] - nums2[j]
        # Say nums1 - nums2 = arr
        # then above can be written as 
        # a[i] <= a[j] + diff -- exactly like Reverse pairs but with <= instead of >
        # This <= instead of > affect the calculation of count only
        # see c += len(right) - j below, since if left[i] <= right[i] + diff
        # this will be true for all remaing j, since they are greater than this value

        def merge_sort(nums):
            if len(nums) <= 1: return 0
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            c_l = merge_sort(left)
            c_r = merge_sort(right)

            # This part we count the pairs
            i = j = c = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    c += (len(right) - j)
                    i += 1
                else:
                    j += 1
            
            # here we do the regular merge of merge sort 
            i = j = k = 0
            while i < len(left) and j < len(right):
                if right[j] < left[i]:
                    nums[k] = right[j]
                    j += 1
                else:
                    nums[k] = left[i]
                    i += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            
            return c_l + c_r + c

        diff_arr = [a - b for (a, b) in zip(nums1, nums2)]
        return merge_sort(diff_arr) 