from heapq  import  heapify,heappush,heappop
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr=[]
        for i in range(len(grid)):
            heapify(grid[i])
            s=len(grid[i])-limits[i]
            while s>0:
                heappop(grid[i])
                s-=1
            arr.append(grid[i])
      
        flattened = [item for arrs in arr for item in arrs]
        heapify(flattened)
        while len(flattened)>k:
            heappop(flattened)
        return sum(flattened)
        


        
           

       
            



         
               