class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        def tripCount(x):
            return sum(x//t for t in time)
        l, r = 1, min(time)*totalTrips
        while l<r:
            mid = (l+r)//2
            if tripCount(mid)<totalTrips:
                l = mid+1
            else:
                r = mid
        return l