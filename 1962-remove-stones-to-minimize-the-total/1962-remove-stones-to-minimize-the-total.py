from heapq import heappush,heappop,heapify
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapify(piles)
        while k>0:
            x = heappop(piles)
            heappush(piles,-ceil(-x/2))
            k -= 1
        return -sum(piles)