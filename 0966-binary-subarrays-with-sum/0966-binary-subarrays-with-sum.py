from collections import  defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        self.nums=nums
        self.goal=goal
        prefix=0
        self.ans=[]
        for i in range(len(nums)):
            prefix+=nums[i]
            self.ans.append(prefix)
        hashmap1=defaultdict(int)
        hashmap1[0]=1
        count=0
       
        for i in range(len(self.ans)):
            if self.ans[i]-self.goal in hashmap1:
                count+=hashmap1[self.ans[i]-self.goal]
            hashmap1[self.ans[i]]+=1
        return count




    


        
  
       

        
    