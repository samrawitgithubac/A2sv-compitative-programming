class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # Split the string into a list of words
        for i in range(len(words)):
            words[i] = words[i][::-1]  # Reverse each word using slicing
        
        return ' '.join(words) 