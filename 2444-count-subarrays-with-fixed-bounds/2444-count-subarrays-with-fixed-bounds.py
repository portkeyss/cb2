class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        miLastIdx = mxLastIdx = -1
        wall = -1
        res = 0
        for i,x in enumerate(nums):
            if x>maxK or x<minK:
                miLastIdx = mxLastIdx = -1
                wall = i
                continue
            if x==minK:
                miLastIdx = i
            if x==maxK:
                mxLastIdx = i
            if miLastIdx>-1 and mxLastIdx>-1:
                b = min(miLastIdx, mxLastIdx)
                res += b-wall #b-wall is the all the possible starting indices of a subarray that ends at current index i
        return res