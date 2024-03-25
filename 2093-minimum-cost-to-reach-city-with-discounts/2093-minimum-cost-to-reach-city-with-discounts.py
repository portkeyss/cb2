class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        edges = [[] for _ in range(n)]
        for c1,c2,t in highways:
            edges[c1].append([c2,t])
            edges[c2].append([c1,t])
        q = [(0,0,discounts)]
        fee = [[inf]*(discounts+1) for _ in range(n)]
        fee[0][discounts] = 0
        while q:
            cost, city, dis = heapq.heappop(q)
            if city==n-1: return cost
            for nei,t in edges[city]:
                if dis>0:
                    x = cost+t//2
                    if x<fee[nei][dis-1]:
                        heapq.heappush(q,(x,nei,dis-1))
                        fee[nei][dis-1]=x
                y = cost+t
                if y<fee[nei][dis]:
                    heapq.heappush(q,(y,nei,dis))
                    fee[nei][dis]=y
        return -1