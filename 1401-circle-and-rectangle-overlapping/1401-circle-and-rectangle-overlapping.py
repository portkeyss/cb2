class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        epsilon = 0.001
        r = radius
        x1 -= xCenter
        x2 -= xCenter
        y1 -= yCenter
        y2 -= yCenter
        if r<x1 or -r>x2 or r<y1 or -r>y2: return False
        if x1<=0 and x2>=0 and y1<=0 and y2>=0: return True
        if r>=abs(x1):
            ya = sqrt(r*r-x1*x1)
            yb = -ya
            if ya>=y1-epsilon and yb<=y2+epsilon: return True
        if r>=abs(x2):
            ya = sqrt(r*r-x2*x2)
            yb = -ya
            if ya>=y1-epsilon and yb<=y2+epsilon: return True
        if r>=abs(y1):
            xa = sqrt(r*r-y1*y1)
            xb = -xa
            if xa>=x1-epsilon and xb<=x2+epsilon: return True
        if r>=abs(y2):
            xa = sqrt(r*r-y2*y2)
            xb = -xa
            if xa>=x1-epsilon and xb<=x2+epsilon: return True
        return False