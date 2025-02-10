class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0
        n=len(matrix)
        j=n-1

        while i<j:
            temp=matrix[i].copy()
            matrix[i]=matrix[j].copy()
            matrix[j]=temp.copy()
            i+=1
            j-=1
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=(matrix[j][i],matrix[i][j])