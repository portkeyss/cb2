class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def md(i,j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
        
        total = 0
        explored = set()
        unexplored = [(0,0)]
        count = 0
        while count<n:
            cost, winner = heapq.heappop(unexplored)
            if winner in explored: continue
            total += cost
            count += 1
            explored.add(winner)
            for nei in range(n):
                if nei not in explored:
                    heapq.heappush(unexplored,(md(winner,nei), nei))
        return total