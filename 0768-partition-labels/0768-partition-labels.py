from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastoccurance={char:i for i, char in enumerate(s)}
        partions=[]
        start=0
        end=0
        
        for i,char in enumerate(s):
            end=max(end,lastoccurance[char])
            if i==end:
                partions.append(end-start+1)
                start=i+1
        return partions

            
        
        
        
