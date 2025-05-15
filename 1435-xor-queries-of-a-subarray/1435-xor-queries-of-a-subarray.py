class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[]
        xor=0
        ans=[]
        for  num in arr:
            xor^=num
            prefix.append(xor)
        for a,b  in queries:
            if a-1>=0:
                ans.append(prefix[b]^prefix[a-1])
            else:
                ans.append(prefix[b])
        return ans

        