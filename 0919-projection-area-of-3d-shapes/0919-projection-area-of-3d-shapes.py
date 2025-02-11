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
        
        '''for i in range(len(grid)):
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
           
        return (count+a1+a2)'''

                
        
               


        