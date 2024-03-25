class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        self.res = inf
        @lru_cache(None)
        def dfs(j,A):
            if j==n:
                self.res = min(self.res, sum(x!=0 for x in A))
                return
            for i in range(n):
                if A[i]+tasks[j]<=sessionTime:
                    B = list(A)
                    B[i] += tasks[j]
                    B.sort()
                    dfs(j+1,tuple(B))
        
        dfs(0,tuple([0]*n))
        return self.res