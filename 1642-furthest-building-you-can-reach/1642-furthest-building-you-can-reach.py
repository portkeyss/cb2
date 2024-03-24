class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        brickAllocate = []
        usedBricks = 0
        for i in range(len(heights)-1):
            climb = heights[i+1]-heights[i]
            if climb <= 0:
                continue
            else:
                heapq.heappush(brickAllocate, -climb)
                usedBricks += climb
                if usedBricks > bricks:
                    usedBricks -= -heapq.heappop(brickAllocate)
                    ladders -= 1
                    if ladders < 0:
                        return i
        return len(heights)-1