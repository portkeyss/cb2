class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i,x in enumerate(nums):
            while dq and dq[0][0]<i-k:
                dq.popleft()
            y = dq[0][1]+x if dq else x
            while dq and dq[-1][1]<=y:
                dq.pop()
            dq.append((i,y))
        return dq[-1][1]