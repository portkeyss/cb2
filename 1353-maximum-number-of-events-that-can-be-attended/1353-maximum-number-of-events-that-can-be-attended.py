class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        hq = []
        ans = 0
        i = 0
        curTime = 0
        while i<n or hq:
            while hq and hq[0]<curTime:
                heapq.heappop(hq)
            if not hq and i<n:
                curTime = events[i][0]
            while i<n and events[i][0]==curTime:
                heapq.heappush(hq, events[i][1])
                i += 1
            if hq:
                heapq.heappop(hq)
                ans += 1
                curTime += 1
        return ans