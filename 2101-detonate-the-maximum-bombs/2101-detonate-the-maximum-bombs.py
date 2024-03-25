class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        edges = [[] for _ in range(n)]     
        for i in range(n-1):
            for j in range(i+1,n):
                x1,y1,r1, x2,y2,r2 = bombs[i][0], bombs[i][1], bombs[i][2], bombs[j][0], bombs[j][1], bombs[j][2]
                dsqr = (x1-x2)**2+(y1-y2)**2
                if dsqr<=r1*r1:
                    edges[i].append(j)
                if dsqr<=r2*r2:
                    edges[j].append(i)
        
        res = 0
        for i in range(n):
            q = deque()
            visited = set()
            q.append(i)
            visited.add(i)
            count = 0 
            while q:
                x = q.popleft()
                count += 1
                for y in edges[x]:
                    if y not in visited:
                        q.append(y)
                        visited.add(y)
            res = max(res, count)
            
        return res