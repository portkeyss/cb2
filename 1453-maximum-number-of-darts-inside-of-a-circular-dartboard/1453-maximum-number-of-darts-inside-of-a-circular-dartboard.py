class Solution:
    def numPoints(self, darts: List[List[int]], r: int) -> int:
        n = len(darts)
        epsilon=10**(-8)

        def inside(dx,dy):
            return dx**2+dy**2<=r**2+epsilon
        
        def findCircle(p1,p2):
            x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
            x12,y12 = (x1+x2)/2.0,(y1+y2)/2.0
            a = (x1-x2)**2+(y1-y2)**2
            if a==4*r*r: return [[x12,y12]]
            if a>4*r*r: return []
            b,c = sqrt(r*r-a/4.),sqrt(a)
            cx1,cy1 = x12+b*(y1-y2)/c,y12-b*(x1-x2)/c
            cx2,cy2 = x12-b*(y1-y2)/c,y12+b*(x1-x2)/c
            return [[cx1,cy1],[cx2,cy2]]

        def tally(cx,cy):
            ans = sum(inside(x-cx,y-cy) for x,y in darts)
            return ans

        res = 1 #even if no 2-points-and-radius-determined circle exists, we always can draw a circle that contains any one of the points
        for i in range(n):
            for j in range(i+1,n):
                for cx,cy in findCircle(darts[i],darts[j]):
                    res = max(res, tally(cx,cy))
        return res