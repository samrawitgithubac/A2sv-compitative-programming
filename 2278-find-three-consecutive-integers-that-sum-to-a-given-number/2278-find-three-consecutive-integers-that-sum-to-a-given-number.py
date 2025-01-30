class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        a= num//3
        print(a)
        if num%3!=0:
            return []
        else:
            return[a-1,a,a+1]