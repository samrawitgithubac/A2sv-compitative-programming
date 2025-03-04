from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_counter=Counter(s)
        res=[]
        if  s_counter['1']==1 and s_counter['0']>0:
            res.append('0'*s_counter['0']) 
            res.append("1")
            ''.join(res)
            return str(''.join(res))
        elif  s_counter['1']>1 and  s_counter['0']>0:
            res.append('1')
            s_counter['1']-=1
            while  s_counter['1']>1:
                res.append('1')
                s_counter['1']-=1

           
            res.append('0'*s_counter['0']) 
            res.append('1')
            ''.join(res)
            return str(''.join(res))
        elif s_counter['0']==0:
            return s
        

            



    

        
        
           
        