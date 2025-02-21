class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0] * len(nums)
        for start, end in requests:
            prefix[start] += 1
            if end+1 < len(nums):
                prefix[end+1] -= 1
        
        for i in range(1, len(nums)):
            prefix[i] += prefix[i-1]
        
        nums.sort(reverse= True)
        temp = []
        for i, val in enumerate(prefix):
            temp.append((i, val))
        sorted_indices = sorted(temp, key=lambda x: x[1], reverse=True)
       
        permute = [0] * len(temp)
        for j, (index, _) in enumerate(sorted_indices):
            
           
            permute[index] = nums[j]
        

        for i in range(1, len(permute)):
            permute[i] += permute[i-1]
        final = 0
        for start, end in requests:
            if start > 0:
                answer = permute[end]-permute[start-1]
                final += answer
            else:
                answer = permute[end]
                final += answer
        return final % (10**9 + 7)



        
       
             
           

            


        
        

    
       


        