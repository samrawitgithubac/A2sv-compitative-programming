class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        ans=[]
        if k>0:

            ans=nums[-k:]
            p=len(nums)-k
            for i in range(p):
                ans.append(nums[i])
            
            nums[:]=ans
        else:
            return nums
        
        
            
            
       
        
       
        
        
         
         
          

       
       


        
    
        
    