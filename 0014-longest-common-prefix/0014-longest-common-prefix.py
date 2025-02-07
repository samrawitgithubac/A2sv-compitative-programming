class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l=0
        s=[]
        i=0
        while i<len(strs[0]) and i<len(strs[len(strs)-1]):
            if strs[0][l]==strs[len(strs)-1][l]:
                s.append(strs[0][l])
                i+=1
                l+=1
            else:
                break
        return "".join(s)



       