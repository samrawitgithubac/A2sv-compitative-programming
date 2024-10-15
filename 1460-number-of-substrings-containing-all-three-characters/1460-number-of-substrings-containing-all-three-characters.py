class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Initialize the last seen positions of 'a', 'b', and 'c' to -1
        a = b = c = -1
        res = 0
        
        # Iterate over the string
        for i, char in enumerate(s):
            # Update the positions of 'a', 'b', or 'c' when we see them
            if char == 'a':
                a = i
            elif char == 'b':
                b = i
            elif char == 'c':
                c = i
            
            # If all of 'a', 'b', and 'c' have been seen at least once
            if a != -1 and b != -1 and c != -1:
                # The smallest index among a, b, c tells us where the valid substring starts
                res += min(a, b, c) + 1
        
        return res
