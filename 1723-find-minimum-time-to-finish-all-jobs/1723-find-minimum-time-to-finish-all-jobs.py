class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        @lru_cache(None)
        def dfs(cur, _cap):
            if cur==n: return True
            for i in range(k):
                if _cap[i]>=jobs[cur]:
                    cap = list(_cap)
                    cap[i]-=jobs[cur]
                    cap.sort()
                    if dfs(cur+1,tuple(cap)): return True
            return False     
            
        left, right = max(jobs), sum(jobs)
        while left<right:
            mid = (left+right)//2
            cap = [mid]*k
            if dfs(0,tuple(cap)):
                right = mid
            else:
                left = mid+1
        return right