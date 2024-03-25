class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        restrictions.sort()
        if restrictions[-1][0]<n: restrictions.append([n,n-1])
        for i in range(1,len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1],restrictions[i-1][1]+restrictions[i][0]-restrictions[i-1][0])
        for i in range(len(restrictions)-2,0,-1):
            restrictions[i][1] = min(restrictions[i][1],restrictions[i+1][1]+restrictions[i+1][0]-restrictions[i][0])
        res = 0
        for i in range(1,len(restrictions)):
            x0, y0, x1, y1 = restrictions[i-1][0], restrictions[i-1][1],restrictions[i][0], restrictions[i][1]
            h = (y0+y1-x0+x1)//2
            res = max(res, h)
        return res  