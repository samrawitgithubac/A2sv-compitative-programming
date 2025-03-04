class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        countof5=0
        countof10=0
        for i in range(len(bills)):
            if bills[i]==5:
                countof5+=1
            elif bills[i]==10:
                if countof5:
                    countof5-=1
                    countof10+=1
                else:
                    return False
               
            elif bills[i]==20:
                if countof10 and countof5:
                    countof5-=1
                    countof10-=1
                elif countof5>=3:
                    countof5-=3
                else:
                    return False
        return True
                    


       
            
              
            
              
            
            



                    

                    




