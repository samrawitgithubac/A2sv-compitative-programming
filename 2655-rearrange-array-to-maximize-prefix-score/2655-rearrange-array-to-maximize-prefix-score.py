class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        prefix=0
        res=[]
        count=0
        for  num  in nums:
            prefix+=num
            if prefix>0:
                count+=1
            else:
                break
                
           
       
        
        return count