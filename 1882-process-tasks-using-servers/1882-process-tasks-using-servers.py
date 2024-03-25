class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        freeServers = [(w,i) for i,w in enumerate(servers)]
        heapq.heapify(freeServers)
        busyServers = []
        res = []
        for j,t in enumerate(tasks):
            while busyServers and busyServers[0][0] <= j:
                tm,w,idx = heapq.heappop(busyServers)
                heapq.heappush(freeServers, (w,idx))
            if freeServers:
                w,idx = heapq.heappop(freeServers)
                heapq.heappush(busyServers,(j+t,w,idx))
                res.append(idx)
            else:
                tm,w,idx = heapq.heappop(busyServers)
                heapq.heappush(busyServers,(tm+t,w,idx))
                res.append(idx)
        return res