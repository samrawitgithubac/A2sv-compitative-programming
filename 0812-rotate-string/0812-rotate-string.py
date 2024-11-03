class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        for i in range(len(s)):
            if ''.join(s)==goal:
                return True
            else:
                s.append(s[0])
                s.pop(0)
        return False
       