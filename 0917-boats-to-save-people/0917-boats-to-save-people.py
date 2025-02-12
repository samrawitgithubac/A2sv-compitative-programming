class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count=0
        i=0
        j=len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                j-=1
                i+=1
                count+=1
            else:
                j-=1
                count+=1
        return count


        
        
                



        
      

       
