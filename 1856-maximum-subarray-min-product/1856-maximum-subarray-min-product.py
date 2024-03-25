class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        A = [None]*n
        B = [None]*n
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            A[i] = stack[-1] if stack else -1
            stack.append(i)
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[i] <= nums[stack[-1]]:
                stack.pop()
            B[i] = stack[-1] if stack else n
            stack.append(i)
        prefix = [0]
        for i in range(n):
            prefix.append(nums[i]+prefix[-1])
        res = 0
        for i in range(n):
            res = max(res, nums[i]*(prefix[B[i]]-prefix[A[i]+1]))
        return res%(10**9+7)