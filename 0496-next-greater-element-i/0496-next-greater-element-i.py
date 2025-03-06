from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        nums1_index = {num: i for i, num in enumerate(nums1)}
        
       
        res = [-1] * len(nums1)
        
      
        stack = []
        
      
        for num in nums2:
           
            while stack and num > stack[-1]:
               
                top = stack.pop()
                
                if top in nums1_index:
                    res[nums1_index[top]] = num
          
            stack.append(num)
        
        return res