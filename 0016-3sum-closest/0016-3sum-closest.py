class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        difference=float('inf')
        ans=0
        
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            closestsum=0
            
            while l<r:
                closestsum=nums[i]+nums[l]+nums[r]
                if difference > abs(target-closestsum):
                    ans=closestsum
                    difference  = min(difference,abs(target-closestsum))
                    
                if closestsum <target:

                    l+=1
                else:
                    r-=1
        return ans
                
            
    
            
        


                
                


        