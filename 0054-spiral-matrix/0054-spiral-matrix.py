class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        return m and [*m[0]]+self.spiralOrder([*zip(*m[1:])][::-1])