class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  
        
        for i in range(1, numRows): 
            row = [1]  
            last_row = res[-1]  
            
            
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
                
            row.append(1)  
            res.append(row)  
        return res



