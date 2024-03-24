class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        hq = []
        for r in restaurants:
            if (veganFriendly == 1 and r[2] == 0) or maxPrice < r[3] or maxDistance < r[4]:
                continue
            heapq.heappush(hq, (-r[1],-r[0]))
        res = []
        while hq:
            res.append(-heapq.heappop(hq)[1])
        return res