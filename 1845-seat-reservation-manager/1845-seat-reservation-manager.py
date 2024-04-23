from sortedcontainers import SortedList
class SeatManager:

    def __init__(self, n: int):
        self.marks = SortedList()
        for i in range(1,n+1):
            self.marks.add(i)

    def reserve(self) -> int:
        return self.marks.pop(0)

    def unreserve(self, seatNumber: int) -> None:
        self.marks.add(seatNumber)
            


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)