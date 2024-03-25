class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        neis = [[] for _ in range(n+1)]
        indegree = [0]*(n+1)
        for a,b in relations:
            neis[a].append(b)
            indegree[b]+=1
        
        hq = []
        A = [0]*(n+1)
        for i in range(1,n+1):
            if indegree[i]==0:
                heapq.heappush(hq,(time[i-1],i))
                A[i] = time[i-1]

        while hq:
            m,i = heapq.heappop(hq)
            for j in neis[i]:
                A[j] = max(A[j],m+time[j-1])
                indegree[j] -= 1
                if indegree[j]==0:
                    heapq.heappush(hq,(A[j],j))
        return max(A)