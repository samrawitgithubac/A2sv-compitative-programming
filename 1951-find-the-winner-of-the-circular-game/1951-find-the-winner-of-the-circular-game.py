class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Create a list of players
        res = list(range(1, n + 1))  # Start with a 1-based index
        
        index = 0  # Start counting from the first player
        while len(res) > 1:
            index = (index + k - 1) % len(res)  # Find the index of the person to eliminate
            res.pop(index)  # Remove that person from the list
        
        return res[0]