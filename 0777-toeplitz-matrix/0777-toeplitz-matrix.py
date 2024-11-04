class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            j=1
            while j<len(matrix[i]):
                 if len(matrix[i])>1 and matrix[i-1][j-1]!=matrix[i][j]:
                    return False
                 j+=1
            
        return True


            

        