class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def f(x):
            pre = position[0]
            ct = 1
            for p in position[1:]:
                if p - pre >= x:
                    ct += 1
                    pre = p
            return ct
        
        l, r = 1, position[-1]-position[0]
        while l < r:
            mid = ceil((l+r)/2)
            if f(mid) < m:
                r = mid-1
            else:
                l = mid
        return l