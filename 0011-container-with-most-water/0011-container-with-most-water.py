class Solution:
    def maxArea(self, height: List[int]) -> int:

        #length of height
        n=len(height) 

        # starting and last index of array
        l,r=0,n-1 

        # initailly result is zero
        res=0 

        while l<r: 
            #storing max area of water in res for every iteration
            res=max(res,(r-l)*min(height[l],height[r])) 

            #updating the smallest vertical line hoping 
            #there would be a bigger vertical line after updation.
            if height[l]<height[r]: 
                l+=1
            else:
                r-=1
        return res
        