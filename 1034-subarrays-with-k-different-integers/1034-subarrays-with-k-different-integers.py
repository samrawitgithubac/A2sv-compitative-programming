class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def countSubarrays(nums, k):
            freq = {}
            dist_count = 0
            total_subarrays = 0
            left, right = 0, 0
            while right < len(nums):
                if nums[right] in freq:
                    freq[nums[right]] += 1
                else:
                    dist_count += 1
                    freq[nums[right]] = 1
                
                while dist_count > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                        dist_count -= 1
                    left += 1
                
                total_subarrays += right - left + 1
                right += 1
            
            return total_subarrays
        
        return countSubarrays(nums, k) - countSubarrays(nums, k-1)