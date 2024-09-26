class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        q=s.split()
        n=len(q)
        return len(q[n-1])
        
            
            

        