class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Use two hashmaps (dictionaries) to store character mappings
        hashmap1 = {}
        hashmap2 = {}
        
        for i in range(len(s)):
            # Check if the character mappings already exist
            if s[i] in hashmap1:
                if hashmap1[s[i]] != t[i]:
                    return False
            else:
                hashmap1[s[i]] = t[i]
            
            if t[i] in hashmap2:
                if hashmap2[t[i]] != s[i]:
                    return False
            else:
                hashmap2[t[i]] = s[i]
                
        return True


        