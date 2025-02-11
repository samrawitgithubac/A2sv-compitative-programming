class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count=0
        
        maxrow=0
        a1=0
        a2=0
        for i in range(len(grid)):
            maxcolumn=0
            for j in range(len(grid[i])):
                if grid[i][j]>0:
                    count+=1
                maxrow=max(grid[i])
                maxcolumn=max(maxcolumn,grid[j][i])
            a1+=maxrow
            a2+=maxcolumn
        return (count+a1+a2)
        
       
                
        
               


        