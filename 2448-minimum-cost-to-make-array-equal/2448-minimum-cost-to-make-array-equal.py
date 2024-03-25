class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        A = Counter()
        for x,c in zip(nums,cost):
            A[x] += c
        keys = sorted(A.keys())
        nums= list(keys)
        cost = [A[num] for num in nums]
        
        f = sum((num-nums[0])*c for num,c in zip(nums,cost))
        cost1 = 0
        cost2 = sum(cost)
        res = f
        for i in range(1,len(nums)):
            cost1 += cost[i-1]
            cost2 -= cost[i-1]
            delta = (nums[i]-nums[i-1])*(cost1-cost2)
            f += delta
            res = min(res,f)
        return res