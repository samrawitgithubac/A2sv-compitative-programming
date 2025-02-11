class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        count=0
        maxcolumn=0
        maxrow=0
        a1=0
        a2=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    count+=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
               
                maxcolumn=max(maxcolumn,grid[i][j])
            print(maxcolumn)
            a1+=maxcolumn
            maxcolumn=0
            
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                
                maxrow=max(maxrow,grid[j][i])
            a2+=maxrow
            maxrow=0
           
        return (count+a1+a2)

                
        
               


        