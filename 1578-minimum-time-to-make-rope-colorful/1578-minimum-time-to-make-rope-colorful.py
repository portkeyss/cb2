class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(s):
            j = i
            maxDupCost = 0
            sumDupCost = 0 
            while j < len(s) and s[j] == s[i]:
                maxDupCost = max(maxDupCost, cost[j])
                sumDupCost += cost[j]
                j += 1
            ans += sumDupCost - maxDupCost
            i = j
        return ans