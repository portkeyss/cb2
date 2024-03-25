class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        prefix = 0
        for i,cost in enumerate(costs):
            prefix += cost
            if prefix>coins:
                return i
        return len(costs)