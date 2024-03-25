from heapq import heappush,heappop
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        m = max(i+days[i] for i in range(n))
        hq = []
        res = 0
        for i in range(m):
            while hq and hq[0][0]<i:
                heappop(hq)
            if i<n and apples[i]>0:
                heappush(hq,(i+days[i]-1,apples[i]))
            if hq and hq[0][0]>=i:
                res += 1
                x,y = heappop(hq)
                y -= 1
                if y>0:
                    heappush(hq,(x,y))
        return res