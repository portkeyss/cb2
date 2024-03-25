class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        t = times[targetFriend][0]
        times.sort(key=lambda x:x[0])
        #use 2 heaps
        pq = []
        availables = []
        for s,e in times:
            while pq and s>=pq[0][0]:
                heapq.heappush(availables, heapq.heappop(pq)[1])
            if not availables:
                availables = [len(pq)]
            chair = heapq.heappop(availables)
            if s==t: return chair
            heapq.heappush(pq,(e,chair))