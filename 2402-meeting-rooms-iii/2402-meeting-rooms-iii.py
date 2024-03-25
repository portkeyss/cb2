from heapq import heappush,heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        hq1 = [] #room availbility sorted by time
        hq2 = [] #for already available rooms, time order become no longer relevant, and availble rooms have to be sorted by index
        useFreq = [0]*n
        for i in range(n):
            heappush(hq1,(0,i))
        for s,e in meetings:
            while hq1 and hq1[0][0]<=s:
                heappush(hq2,heappop(hq1)[1])
            if hq2:
                room = heappop(hq2)
                heappush(hq1,(e,room))
            else:
                t, room = heappop(hq1)
                heappush(hq1,(t+e-s,room))
            useFreq[room] += 1
        x = max(useFreq)
        return useFreq.index(x)