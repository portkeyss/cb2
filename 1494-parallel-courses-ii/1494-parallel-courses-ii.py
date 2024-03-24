from itertools import combinations
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        neis = [[] for _ in range(n)]
        incoming = [0]*n
        for a,b in relations:
            neis[a-1].append(b-1)
            incoming[b-1]+=1

        @lru_cache(None)
        def f(mask,indegree):
            if mask==(1<<n)-1: return 0
            ans = inf
            cand = [i for i in range(n) if mask&(1<<i)==0 and indegree[i]==0]
            for comb in combinations(cand, min(k,len(cand))):
                newMask, newIndegree = mask, list(indegree)
                for i in comb:
                    newMask |= (1<<i)
                    for j in neis[i]:
                        newIndegree[j] -= 1
                ans = min(ans,1+f(newMask,tuple(newIndegree)))
            return ans
                
        return f(0,tuple(incoming))