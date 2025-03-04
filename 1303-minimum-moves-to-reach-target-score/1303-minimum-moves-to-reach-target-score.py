class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        if target==1:
            return 0
        else:
            while  target>1 and maxDoubles>0:
                count+=(target%2)+1
                target=target//2
                maxDoubles-=1
            count+=target-1
            return count
               
                
                
            
            

            
                
       