class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hashmap1 = {}
        charss = 64
        res = []
        
        for i in range(1, 27):
            charss += 1
            hashmap1[i] = chr(charss)
        
        while columnNumber > 0:
            columnNumber -= 1  
            remainder = columnNumber % 26
            res.append(hashmap1[remainder + 1])
            columnNumber //= 26
        
        return "".join(res[::-1])
