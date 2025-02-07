class Solution:
    def findWords(self, words: List[str]) -> List[str]:
       
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")
        res=[]
        for word in words:
            lowerWord=set(word.lower())
            if lowerWord.issubset(row1) or lowerWord.issubset(row2) or lowerWord.issubset(row3):
                res.append(word)
        return res

        

        
        

        
        