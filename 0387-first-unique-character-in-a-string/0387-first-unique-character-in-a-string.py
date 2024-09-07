class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_set={}
        for char in s:
             hash_set[char]= hash_set.get(char,0)+1
        for index, char in enumerate(s):

            if hash_set[char] == 1:
                return index
        return -1
        
            
       

        

       
      




            
             

       
        