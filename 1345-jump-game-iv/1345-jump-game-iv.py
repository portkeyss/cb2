class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx = defaultdict(list)
        for i, p in enumerate(arr):
            idx[p].append(i)
        n = len(arr)
        if n == 1:
            return 0
        q = deque()
        q.append(0)
        dist = [n]*n
        dist[0] = 0
        while q:
            i = q.popleft()
            if i-1 >= 0 and dist[i-1]==n:
                q.append(i-1)
                dist[i-1] = dist[i]+1
            if i+1 >= 0 and dist[i+1]==n:
                q.append(i+1)
                dist[i+1] = dist[i]+1
                if i+1==n-1:
                    return dist[i+1] 
            while idx[arr[i]]:
                j = idx[arr[i]].pop()
                if dist[j] == n:
                    q.append(j)
                    dist[j] = dist[i]+1
                    if j == n-1:
                        return dist[j]
            