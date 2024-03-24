class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        hq = []
        ans = 0
        for l in light:
            heapq.heappush(hq,-l)
            if -hq[0] == len(hq):
                ans += 1
        return ans