class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        x, y = 1, 1
        for _ in range(2,n+1):
            x, y = (3*x+2*y)%mod, (2*x+2*y)%mod
        return (((x+y)%mod)*6)%mod