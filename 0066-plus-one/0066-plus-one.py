class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=map(str,digits)
        
        digits="".join(digits)
        digits=int(digits)+1
        digits=str(digits)
        res=[]
        for i in range(len(digits)):
            res.append(int(digits[i]))
        return res

       
       
        
       

    

       