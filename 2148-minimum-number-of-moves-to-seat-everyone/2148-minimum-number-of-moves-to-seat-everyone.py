class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        
        sums=0
        for i in range(len(students)):
            sums+=abs(students[i]-seats[i])
        return sums
            
                
            


           
            


        