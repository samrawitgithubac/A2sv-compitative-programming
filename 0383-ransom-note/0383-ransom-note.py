class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        
        # Count characters in magazine
        for i in range(len(magazine)):
            if magazine[i] in hashmap1:
                hashmap1[magazine[i]] += 1
            else:
                hashmap1[magazine[i]] = 1
                
        # Count characters in ransomNote
        for i in range(len(ransomNote)):
            if ransomNote[i] in hashmap2:
                hashmap2[ransomNote[i]] += 1
            else:
                hashmap2[ransomNote[i]] = 1
                
        # Check if magazine has enough of each character in ransomNote
        for i in range(len(ransomNote)):
            a = ransomNote[i]
            if hashmap1.get(a, 0) < hashmap2[a]:
                return False
                
        return True
