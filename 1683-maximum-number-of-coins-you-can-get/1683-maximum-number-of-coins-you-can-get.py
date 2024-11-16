class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        for _ in range(len(piles)//3):
            piles.pop()
            res += piles.pop()
            piles.pop(0)
        
        return res

        