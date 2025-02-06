class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        value=[]
        innermatrxi=[[] for _ in range(len(matrix[0]))]
       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                innermatrxi[j].append(matrix[i][j])
        for i in  innermatrxi:
            value.append(i)
        return value
    

               



        
        
       
        
       



    
        