class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q1 = deque()
        q2 = deque()
        res = 0
        j = -1
        for i,x in enumerate(nums):
            while q1 and q1[-1][1]<=x: q1.pop()
            q1.append((i,x))
            while q2 and q2[-1][1]>=x: q2.pop()
            q2.append((i,x))
            while q1[0][1]-q2[0][1]>limit:
                if q1[0][0]<q2[0][0]: 
                    j = q1.popleft()[0]
                else:
                    j = q2.popleft()[0]
            res = max(res,i-j)
        return res