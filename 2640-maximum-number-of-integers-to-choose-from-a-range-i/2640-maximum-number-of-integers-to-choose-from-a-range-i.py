class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned=set(banned)
        sum, cnt=0, 0
        for x in range(1, n+1):
            if x not in banned:
                sum+=x
                if sum>maxSum: break
                cnt+=1
        return cnt