class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        A = [a-b for a,b in zip(nums1, nums2)]
        A.sort()
        res = 0
        n = len(A)
        for a in A: #find pairs A[i]+A[j]>0
            k = bisect.bisect(A, -a)
            res += n-k if a<=0 else n-k-1
        return res//2