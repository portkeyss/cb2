class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n,m = len(colors), len(edges)
        neis = [[] for _ in range(n)]
        indegree = [0]*n
        for s,e in edges:
            neis[s].append(e)
            indegree[e] += 1
        
        #Kahn's alg, topological sort
        S = deque()
        nodes = 0
        res = 0
        count = [Counter() for _ in range(n)]
        for i in range(n):
            if indegree[i]==0: 
                S.append(i)
                count[i][colors[i]]=1

        while S:
            x = S.popleft()
            nodes += 1
            res = max(res, count[x][colors[x]])
            for y in neis[x]:
                indegree[y] -= 1
                for ch in string.ascii_lowercase:
                    count[y][ch] = max(count[y][ch], count[x][ch]+(ch==colors[y]))
                if indegree[y] == 0: S.append(y)

        if nodes<n: return -1
        return res