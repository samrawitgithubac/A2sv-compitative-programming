from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxstorage=max(costs)+1
        sortedcosts=[0]*maxstorage
        ans=[]
        for i,value in  enumerate(costs):
            if sortedcosts[value]==0:
                sortedcosts[value]=1
            else:
                sortedcosts[value]+=1
        for i in range(len(sortedcosts)):
            for j in range(sortedcosts[i]):
                ans.append(i)
       
        sums=0
        count=0
        for i in ans:
            if sums+i<=coins:
                sums+=i
                count+=1
           
        return count

        

       


    

                
            
      
        
       
       
        
