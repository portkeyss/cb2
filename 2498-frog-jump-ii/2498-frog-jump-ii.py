class Solution:
    def maxJump(self, stones: List[int]) -> int:
        #there must exist an optimal solution where all stones are used
        n = len(stones)
        if n==2: return stones[-1]-stones[0]
        cur = prev = prevPrev = 0
        for i in range(2,n):
            cur = max(prev, prevPrev, stones[i]-stones[i-1], stones[i]-stones[i-2])
            prev, prevPrev = cur, prev
        return cur