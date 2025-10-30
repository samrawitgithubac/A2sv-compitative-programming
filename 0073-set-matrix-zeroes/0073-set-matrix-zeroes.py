class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ans=[]
        for  i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    ans.append((i,j))
        
        for i,j  in ans:
            for col in range(len(matrix[0])):
                matrix[i][col]=0
            for  row in range(len(matrix)):
                matrix[row][j]=0
        return matrix
        


