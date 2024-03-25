class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n,mi,mx = len(nums),min(nums),max(nums)

        def valid(x):
            inc = 0
            for i in range(n-1,-1,-1):
                inc = max(0,nums[i]+inc-x)
            return inc==0

        l, r = mi, mx
        while l<r:
            mid = (l+r)//2
            if valid(mid): r = mid
            else:l = mid+1
        return l