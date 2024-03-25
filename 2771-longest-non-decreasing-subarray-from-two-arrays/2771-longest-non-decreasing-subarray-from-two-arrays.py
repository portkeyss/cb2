class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        low = high = -inf
        a = b = 0
        res = 0
        for x,y in zip(nums1,nums2):
            x,y = min(x,y), max(x,y)
            if x>=high:
                c = b+1
            elif x>=low:
                c = a+1
            else:
                c = 1
            if y>=high:
                d = b+1
            elif y>=low:
                d = a+1
            else:
                d = 1
            low,high,a,b = x,y,c,d
            res = max(res,a,b)
        return res   