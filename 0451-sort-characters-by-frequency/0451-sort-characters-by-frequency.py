from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap1=Counter(s)
        newstring=dict(sorted(hashmap1.items() ,key=lambda item:item[1], reverse=True))
        s1=[]
        for i ,value in enumerate(newstring):
            while hashmap1[value]>0:
                s1.append(value)
                hashmap1[value]-=1
        return "".join(s1)
                
           
            
            

       
        