class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo, hi = 1, max(quantities)
        while lo<hi:
            mid = (lo+hi)//2
            minStores = sum((q+mid-1)//mid for q in quantities)
            if minStores<=n:
                hi = mid
            else:
                lo = mid+1
        return hi