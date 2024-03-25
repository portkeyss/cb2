class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0]*n
        for x in favorite:
            indegree[x] += 1
        
        visited = [False]*n
        
        q = deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                visited[i] = True
        depth = [0]*n
        while q:
            k = q.popleft()
            l = favorite[k]
            depth[l] = max(depth[l],1+depth[k])
            indegree[l] -= 1
            if indegree[l]==0:
                q.append(l)
                visited[l] = True

        res = 0
        res2 = 0
        for i in range(n):
            if visited[i]: continue
            j = i
            d = 0
            while not visited[j]:
                visited[j] = True
                j = favorite[j]
                d += 1
            if d==2:
                res2 += 2+depth[i]+depth[favorite[i]]
            else:
                res = max(res, d)
        return max(res,res2)