from heapq import heappush,heappop
from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        A = [0]*k
        busy = [] #(timeAvailable,serverIdex)
        available = SortedList() # serverIndex
        for i in range(k):
            available.add(i)
        for i,(a,l) in enumerate(zip(arrival,load)):
            while busy and busy[0][0]<=a:
                available.add(heappop(busy)[1])
            if not available: continue
            j = i%k
            x = available.bisect_right(j-1)
            if x==len(available): x = available.bisect_right(-1)
            server = available.pop(x)
            heappush(busy,(a+l,server))
            A[server] += 1
        mx = max(A)
        return [i for i in range(k) if A[i]==mx]    