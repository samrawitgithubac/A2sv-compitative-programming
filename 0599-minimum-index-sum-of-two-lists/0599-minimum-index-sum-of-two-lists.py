from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2_index = {}
        minIndexSum=float('inf')
        resultStrings=[]
        for i in range(len(list2)):
            list2_index[list2[i]] = i
        
        for i, curr_string in enumerate(list1):
            if  curr_string in list2_index:
                indexSum=i+list2_index[curr_string] 
                if indexSum<minIndexSum:
                    resultStrings=[curr_string]
                elif indexSum==minIndexSum:
                    resultStrings.append(curr_string)
                minIndexSum=min(minIndexSum,indexSum) 
                
                
        
        return resultStrings
        




            
        
            


        