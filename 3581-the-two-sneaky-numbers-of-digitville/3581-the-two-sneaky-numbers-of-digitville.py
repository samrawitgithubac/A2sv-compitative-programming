from collections import  Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter_nums=Counter(nums)
        res=[]
        for i in counter_nums:
            if counter_nums[i]==2:
                res.append(i)
        return res
                

        