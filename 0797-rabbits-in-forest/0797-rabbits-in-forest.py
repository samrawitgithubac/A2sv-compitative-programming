
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt_dict = {}
        res = 0
        for n in answers:
            if n == 0:
                res+=1
            else:
                if n not in cnt_dict or n== cnt_dict[n]:
                    cnt_dict[n] = 0
                    res+=n+1
                else:
                    cnt_dict[n] += 1
                    
        return res