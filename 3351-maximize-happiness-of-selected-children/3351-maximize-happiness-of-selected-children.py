class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count=0
        turns=0
        for i in range(k):
            count+=max(happiness[i]-turns,0)
            turns+=1
        return count
                
       

                    
                    
               
            
           
             

               


        