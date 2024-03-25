class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        #the process can be simulated as a process of shortsell and buying in stocks
        shortsell = -inf
        buy = 0
        for p in nums:
            shortsell, buy = max(shortsell, buy+p), max(buy, shortsell-p)
        return max(shortsell, buy)