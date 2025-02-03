class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
         
        
         s=numBottles
       
         while  numBottles/numExchange>=1:
            a= numBottles//numExchange
            b= numBottles%numExchange
            s+=a
            numBottles=a+b
         return s
              
           

           

            



       

       
           


