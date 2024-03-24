class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = []
        while prices:
            p = prices.pop()
            while stack and stack[-1]>p:
                stack.pop()
            res.append(p-stack[-1] if stack else p)
            stack.append(p)
        return res[::-1]