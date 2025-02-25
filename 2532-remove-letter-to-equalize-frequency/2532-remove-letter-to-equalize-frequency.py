from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        freq = [v for v in c.values()]
        print(freq)
        for i in range(len(freq)):
            freq[i] -= 1
            if len(set(freq)) == 1:
                return True
            if freq[i] == 0:
                if len(set(freq)) == 2:
                    return True
            freq[i] += 1
        return False
        
        


        



                  
        

        

                    

                
               
        
        