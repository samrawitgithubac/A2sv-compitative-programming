class NumMatrix(object):

    def __init__(self, matrix):
        
        self.matrix=matrix
        self.row=len(self.matrix)
        self.col=len(self.matrix[0])
        self.prefixsum=[[0]*self.col for _ in self.matrix]
        for i in range(self.row):
            for j in range(self.col):
                self.prefixsum[i][j]=self.matrix[i][j]
                if i > 0:
                    self.prefixsum[i][j]+=self.prefixsum[i-1][j]
                if j > 0:
                    self.prefixsum[i][j]+=self.prefixsum[i][j-1]
                if i > 0 and j > 0:
                    self.prefixsum[i][j]-=self.prefixsum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        subregion = self.prefixsum[row2][col2]
        if row1 > 0:
            subregion -= self.prefixsum[row1 - 1][col2]
        if col1 > 0:
            subregion -= self.prefixsum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            subregion += self.prefixsum[row1 - 1][col1 - 1]
        return subregion
