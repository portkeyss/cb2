class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dq = deque()
        res = []
        for i in range(n):
            while dq and nums[i]<dq[-1]:
                dq.pop()
            dq.append(nums[i])
            if i==n-k:
                res.append(dq.popleft())
                k -= 1
        return res  