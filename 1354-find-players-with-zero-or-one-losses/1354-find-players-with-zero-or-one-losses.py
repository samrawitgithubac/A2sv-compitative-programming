class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allPlayer=set()
        loss_counter={}
        for  winner,losser in matches:
             allPlayer.add(winner)
             allPlayer.add(losser)
             if losser not in loss_counter:
                loss_counter[losser]=1
             else:
                 loss_counter[losser]+=1
        zero_losser=[i for i in allPlayer if i not in loss_counter ]
        one_losser=[i for i in loss_counter if loss_counter[i]==1 ]
        zero_losser.sort()
        one_losser.sort()
        return [ zero_losser, one_losser]



            


             
        


        
        
       

       


           
            

        





         
            
            


             
       
        
        
      

       
        
       