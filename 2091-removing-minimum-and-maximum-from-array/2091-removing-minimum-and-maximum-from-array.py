class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mx = -inf
        mi = inf
        mxIdx = None
        miIdx = None
        for i,p in enumerate(nums):
            if p>mx:
                mx = p
                mxIdx = i
            if p<mi:
                mi = p
                miIdx = i
        a, b = min(miIdx, mxIdx), max(miIdx, mxIdx)
        return min(b+1, n-a, a+1+n-b)