class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        i=0
        count=0
        for i in range(len(hours)):
            if hours[i]>=target:
                count+=1
        return count
       
        