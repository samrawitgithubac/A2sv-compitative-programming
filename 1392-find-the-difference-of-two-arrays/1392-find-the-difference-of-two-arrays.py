class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
       
        res1=[]
        res2=[]
        for s  in s1:
            if s not in nums2:
                 res1.append(s)
            

           
        for s  in s2:
            if s not in nums1:
                 res2.append(s)
        

           
        return [res1,res2]
       



        