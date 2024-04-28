class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        hq = []
        
        minTime = min(events[i][0] for i in range(n))
        maxTime = max(events[i][1] for i in range(n))
        ans = 0
        i = 0

        for curTime in range(minTime,maxTime+1):
            while hq and hq[0]<curTime:
                heapq.heappop(hq)
            while i<n and events[i][0]==curTime:
                heapq.heappush(hq, events[i][1])
                i += 1
            if hq:
                heapq.heappop(hq)
                ans += 1  
        return ans   