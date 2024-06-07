class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        mi = min(nums)
        mx = max(nums)
        miIdx = nums.index(mi)
        mxIdx = n-1-nums[::-1].index(mx)
        return miIdx+n-1-mxIdx-(miIdx>mxIdx)