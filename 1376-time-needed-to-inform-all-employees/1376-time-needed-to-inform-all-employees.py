class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for _ in range(n)]
        for i,m in enumerate(manager):
            if i!=headID:
                children[m].append(i)
        q = deque()
        dist = [inf]*n
        q.append(headID)
        dist[headID] = 0
        while q:
            m = q.popleft()
            for c in children[m]:
                dist[c] = dist[m]+informTime[m]
                q.append(c)
        return max(dist)