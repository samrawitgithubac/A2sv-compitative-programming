
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt_dict = {}
        ans = 0
        for n in answers:
            if n == 0:
                ans+=1
            else:
                if n not in cnt_dict or n== cnt_dict[n]:
                    cnt_dict[n] = 0
                    ans+=n+1
                else:
                    cnt_dict[n] += 1
                    
        return ans