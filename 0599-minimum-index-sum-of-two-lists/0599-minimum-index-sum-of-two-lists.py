from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mm=defaultdict(list)
        r=0
        res=[]
        minimumIndex= float('inf')
        while r<len(list1):
            minSumIndex=len(list1)+len(list2)
            l=0
            while l<len(list2):
                if list1[r]==list2[l]:
                    minSumIndex=min(minSumIndex,l+r)
                
                l+=1
            if minSumIndex<len(list1)+len(list2):
                
                minimumIndex=min(minSumIndex, minimumIndex)
                mm[minSumIndex].append(list1[r])

        
            r+=1

        return mm[minimumIndex] 

           
          
        

                    
                

           
           
               
               
            


        