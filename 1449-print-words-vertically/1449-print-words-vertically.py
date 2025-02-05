from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()                       # Split the input string into words
        max_len = len(max(words, key=len))      # Find the maximum length of words
        
        result = []                             # List to store vertical words
        
        for col in range(max_len):              # Iterate over each column index
            vertical_word = ''                  # Initialize vertical word
            
            for word in words:                  # Iterate over each word
                if col < len(word):             # If the word has a character at this column
                    vertical_word += word[col]
                else:
                    vertical_word += ' '        # Add space if the word is shorter

            result.append(vertical_word.rstrip())  # Remove trailing spaces
        return result
