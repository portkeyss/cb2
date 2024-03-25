class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        cur = 0
        mx = mi = 0
        for d in differences:
            cur += d
            mx = max(mx,cur)
            mi = min(mi,cur)
        return max(0,upper-lower-mx+mi+1)