class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        
        # Check for single word case before the loop
        if len(sentence) == 1:
            return sentence[0][0] == sentence[0][-1]
        
        i = 0
        while i < len(sentence) - 1:
            if sentence[i][-1] == sentence[i + 1][0]:
                i += 1
            else:
                return False
                
       
        return sentence[i][-1] == sentence[0][0]


