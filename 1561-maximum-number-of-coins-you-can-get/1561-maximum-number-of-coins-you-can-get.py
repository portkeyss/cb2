class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        return sum(piles[i] for i in range(1,len(piles)*2//3+1,2))