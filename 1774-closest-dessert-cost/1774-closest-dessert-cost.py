class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n, m = len(baseCosts), len(toppingCosts)
        toppingPrices = set([0])
        for i in range(m):
            s = set()
            for q in [toppingCosts[i], toppingCosts[i]*2]:
                for p in toppingPrices:
                    s.add(p+q)
            toppingPrices |= s
        lowestDiff = inf
        res = inf
        for base in baseCosts:
            for t in toppingPrices:
                cost = base+t
                diff = abs(cost-target)
                if diff<lowestDiff or diff==lowestDiff and cost<res:
                    res = cost
                    lowestDiff = diff
        return res         