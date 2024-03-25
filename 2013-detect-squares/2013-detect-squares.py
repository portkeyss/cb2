class DetectSquares:

    def __init__(self):
        self.A = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        i,j = point[0], point[1]
        self.A[i][j] += 1

    def count(self, point: List[int]) -> int:
        i,j = point[0], point[1]
        ct = 0
        for y in self.A[i]:
            if y<j:
                edge = j-y
                ct += self.A[i][y]*self.A[i-edge][j]*self.A[i-edge][j-edge]
                ct += self.A[i][y]*self.A[i+edge][j]*self.A[i+edge][j-edge]
            elif y>point[1]:
                edge = y-j
                ct += self.A[i][y]*self.A[i-edge][j]*self.A[i-edge][j+edge]
                ct += self.A[i][y]*self.A[i+edge][j]*self.A[i+edge][j+edge]
        return ct


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)