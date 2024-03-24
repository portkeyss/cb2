class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        #brute force, as implied by small numbers
        m = len(requests)
        ans = 0
        for mask in range(1<<m):
            count = mask.bit_count()
            if count<=ans: continue
            indegree = [0]*n
            for i in range(m):
                if mask&(1<<i):
                    indegree[requests[i][0]] -= 1
                    indegree[requests[i][1]] += 1
            if indegree==[0]*n: ans = count
        return ans