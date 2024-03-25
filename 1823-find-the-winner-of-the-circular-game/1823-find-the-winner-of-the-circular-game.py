class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        seat = [i for i in range(1,n+1)]
        p = 0
        while n>1:
            p = (p+k-1)%n
            if p<n-1:
                seat[p:n-1]=seat[p+1:n]
            else:
                p = 0
            seat.pop()
            n -= 1
        return seat[0]