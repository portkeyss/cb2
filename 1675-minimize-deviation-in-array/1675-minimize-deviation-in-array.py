from sortedcontainers import SortedList
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        for i in nums:
            sl.add(i*2 if i%2==1 else i)
        res = inf
        while len(sl)>=n:
            x = sl.pop()
            y = sl[-(n-1)]
            res = min(res, x-y)
            if x%2==0:
                sl.add(x//2)
        return res