from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        numsCounter=Counter(nums)
        res=[]
        for  i in numsCounter:
            if numsCounter[i]==2:
                res.append(i)
        return res


        