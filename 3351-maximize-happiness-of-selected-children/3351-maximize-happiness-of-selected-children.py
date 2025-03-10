class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        count=happiness[0]
                
        for  i in range(1,len(happiness)):
                if i<k:
                    a=happiness[i]-i
                    if a>=0:
                        count+=happiness[i]-i
                    else:
                        count+=0

                    
                    
        return count
               
            
           
             

               


        