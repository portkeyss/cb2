class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        prev = [[] for _ in range(n)]
        for i,x in enumerate(nums):
            while stack and stack[-1][0]<x:
                prev[i].append(stack.pop()[1])
            stack.append((x,i))

        res = [-1]*n
        hq = []
        for i,x in enumerate(nums):
            while hq and hq[0][0]<x:
                res[heappop(hq)[1]] = x
            for j in prev[i]:
                heappush(hq,(nums[j],j))
        return res