class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = inf
        idx = -1
        for i,(p,q) in enumerate(points):
            if p==x or q==y:
                d = abs(x-p)+abs(y-q)
                if d<dist:
                    dist = d
                    idx = i
        return idx