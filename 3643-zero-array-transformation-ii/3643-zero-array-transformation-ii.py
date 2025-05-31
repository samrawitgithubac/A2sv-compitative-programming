class Solution(object):
    def minZeroArray(self, nums, queries):
        diff = [0] * (len(nums) + 1) 
        total = 0
        count = 0

        for i in range(len(nums)):
            while total + diff[i] < nums[i]: 
                count+=1
                if count > len(queries):  
                    return -1
                
                left, right, val = queries[count-1] 
             

             
               
                if right  >=  i:
                    diff[max(left, i)] += val
                    diff[right + 1] -= val

            total += diff[i] 

        return count
