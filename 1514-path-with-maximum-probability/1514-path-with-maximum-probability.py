class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = [0]*n
        neis = [[] for _ in range(n)]
        for (a,b),p in zip(edges,succProb):
            if p>0:
                neis[a].append([b,p])
                neis[b].append([a,p])
        
        hq = [(-1,start_node)]
        prob[start_node] = 1
        while hq:
            p_neg,x = heapq.heappop(hq)
            if x==end_node: return -p_neg
            if prob[x]<-p_neg: continue
            for y,pr in neis[x]:
                q = p_neg*pr
                if prob[y]==0 or prob[y]<-q:
                    heapq.heappush(hq,(q,y))
                    prob[y] = -q
        return 0