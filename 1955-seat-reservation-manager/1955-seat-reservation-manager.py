from heapq import heapify, heappush, heappop
class SeatManager:

    def __init__(self, n: int):
        self.n=n
        self.arr=[i for i in range(1,n+1)]
        heapify(self.arr)

        
        

    def reserve(self) -> int:
        small=heappop(self.arr)
        return small

        

    def unreserve(self, seatNumber: int) -> None:
        self.seatNumber=seatNumber
        heappush(self.arr,self.seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)