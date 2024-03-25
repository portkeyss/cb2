class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()
        t = 0
        hq = []
        res = []
        i = 0
        curTime = tasks[0][0]
        while len(res) < len(tasks):
            while i<len(tasks) and tasks[i][0] <= curTime:
                heapq.heappush(hq, (tasks[i][1], tasks[i][2]))
                i += 1
            if hq:
                processTime, j = heapq.heappop(hq)
                res.append(j)
                curTime += processTime
            else:
                curTime = tasks[i][0]
        return res