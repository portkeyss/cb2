class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        A = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        speed, efficiency = map(list, zip(*A))
        hq = [] 
        s = 0
        performance = 0
        for i in range(n):
            performance = max(performance, (s + speed[i])* efficiency[i])
            heapq.heappush(hq, speed[i])
            s += speed[i]
            if len(hq) > k-1:       
                s -= heapq.heappop(hq)
        return performance % (10**9 + 7)      