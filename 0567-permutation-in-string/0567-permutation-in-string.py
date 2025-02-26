class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        letterDict = {}
        visited = set()
        
        for letter in s1:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
        
        letterDict = sorted(letterDict.items())

        currWindow, currLen = [], 0
        left = 0
        n, m = len(s2), len(s1)
        currLetterDict = {}

        for right in range(n):
            letter = s2[right]
            currWindow.append(letter)
            currLen += 1

            if letter in currLetterDict:
                currLetterDict[letter] += 1
            else:
                currLetterDict[letter] = 1

            while currLen > m:
                # cannot be an anagram : not enough words
                currWindow.remove(s2[left])
                if s2[left] in currLetterDict:
                    if currLetterDict[s2[left]] == 1:
                        currLetterDict.pop(s2[left])
                    else:
                        currLetterDict[s2[left]] -= 1
                currLen -= 1
                left += 1
            
            if currLen == m:
                sortedDict = sorted(currLetterDict.items())
                if sortedDict == letterDict:
                    return True
        
        return False