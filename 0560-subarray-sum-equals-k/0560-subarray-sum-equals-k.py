from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        ans=[]
        hashmap1=defaultdict(int)
        hashmap1[0]=1
        count=0
        for i in range(len(nums)):
            prefix+=nums[i]
            ans.append(prefix)
        for  i in range(len(ans)):
            if (ans[i]-k) in hashmap1:
                count+=hashmap1[ans[i]-k]
            
            hashmap1[ans[i]]+=1
        return count
                
                
                
       



       
                    


       
        