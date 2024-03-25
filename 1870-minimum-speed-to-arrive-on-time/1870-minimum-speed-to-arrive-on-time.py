class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1 >= hour: return -1
        def duration(v):
            return sum(ceil(d/v) for d in dist[:-1])+dist[-1]/v
        l = 1
        r = max(dist[:-1]+[ceil(dist[-1]/(hour-len(dist)+1))])
        while l<r:
            m = (l+r)//2
            if duration(m) > hour:
                l = m+1
            else:
                r = m
        return r