class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxsum=0
        while i<j:
            
            sums=min(height[i],height[j])*(j-i)
            maxsum=max(maxsum,sums)
            if height[j]>height[i]:
               
                i+=1
            else:
                
                j-=1
        return maxsum
      

       



       