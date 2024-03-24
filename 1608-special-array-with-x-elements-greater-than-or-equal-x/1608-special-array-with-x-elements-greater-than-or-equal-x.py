class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, n
        while lo<=hi:
            y = (lo+hi)//2
            j = bisect.bisect_left(nums, y)
            if y==n-j: return y
            elif y<n-j: lo=y+1
            else: hi=y-1
        return -1