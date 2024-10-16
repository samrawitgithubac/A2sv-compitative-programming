class Solution:

    #This is the Updated version of question count subarray with given sum k from Array Playlist
    #Optimum
    # To Find number of Subarray which matches goal = number of subarray which are less than goal - number of subarray which are lss than goal - 1

    # Eg Goal less than 2 are 10  - Goal less than goal -1 (2) are 5
    # so goal equals to 2 are remaining one  

    def numSubarraysWithSumLessThanGoal(self,nums,goal):
        if goal<0:
            return 0
        left, right = 0,0
        Sum = 0
        count = 0 
        

        while right<len(nums):
            Sum += nums[right]

            # Trim left till we get sum<=goal
            while Sum>goal:
                Sum = Sum - nums[left]
                left+=1
            # if r at 3 and l at 0 so we wil count all possible subarray we can have in between such as 0th , (0th,1), (0th,1 ,2), (0th,1,2,3)
            # = 3 - 0 + 1
            count+= right - left +1
            right+=1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        Ans = self.numSubarraysWithSumLessThanGoal(nums,goal) - self.numSubarraysWithSumLessThanGoal(nums,goal-1)
        return Ans
    