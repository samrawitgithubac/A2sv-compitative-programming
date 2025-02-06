class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=[""]*len(s)
        s=list(s)
        for i in range(len(indices)):
            res[indices[i]]=s[i]
       
        return "".join(res)
        
       

      