class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        i = 0
        n = len(word)
        
        while i < n:
            count = 1
            # Count up to 9 occurrences of the same character
            while i + 1 < n and word[i] == word[i + 1] and count < 9:
                count += 1
                i += 1
            
            # Append the count and the character to the result
            comp.append(str(count))
            comp.append(word[i])
            
            i += 1  # Move to the next character

        return ''.join(comp)
