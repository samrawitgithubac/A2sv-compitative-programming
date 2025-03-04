class Solution(object):
    def canJump(self, nums):
        jump_range=0
        for i in range(len(nums)):
           
            if jump_range<i:
                return False   
            jump_range=max(jump_range,i+nums[i])
        return True
