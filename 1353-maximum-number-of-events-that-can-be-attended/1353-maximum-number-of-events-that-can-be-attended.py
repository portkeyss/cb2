class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        d = events[0][0]
        last_day = max(events[idx][1] for idx in range(len(events)))
        end_min_heap = []
        i = 0
        res = 0
        while d <= last_day:
            while i < len(events) and events[i][0] == d:
                heapq.heappush(end_min_heap, events[i][1])
                i += 1
            if end_min_heap and end_min_heap[0] >= d:
                res += 1
                heapq.heappop(end_min_heap)
            while end_min_heap and end_min_heap[0] == d:
                heapq.heappop(end_min_heap)
            d += 1    
        return res   