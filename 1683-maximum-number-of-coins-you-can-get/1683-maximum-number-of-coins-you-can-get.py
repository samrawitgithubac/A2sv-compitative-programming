class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sums=0
        for _ in range(len(piles)//3):
            piles.pop()
            sums+=piles.pop()
            piles.pop(0)
        return sums


        
        