class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
       
        nums="".join((map(str,nums)))
        lists=[]
        for i in range(len(nums)):
            lists.append(int(nums[i]))
        return lists

       
       

        

      
           

            
            
        