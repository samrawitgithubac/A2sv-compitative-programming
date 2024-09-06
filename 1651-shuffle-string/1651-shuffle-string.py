class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=[""]*len(s)
        for index in range(len(s)):
            last=indices[index]
            char=s[index]
            result[last]=char
        return "".join(result)
       

      