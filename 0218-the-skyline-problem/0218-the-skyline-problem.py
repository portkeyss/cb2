from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        A = SortedList()
        points = set()
        start = defaultdict(list)
        end = defaultdict(list)
        for l,r,h in buildings:
            start[l].append(h)
            end[r].append(h)
            points.add(l)
            points.add(r)
        points = sorted(list(points))
        cur = 0
        ans = []
        for p in points:
            for h in end[p]:
                A.remove(-h)
            for h in start[p]:
                A.add(-h)
            t = -A[0] if A else 0
            if t!=cur: 
                cur = t
                ans.append([p,cur])
        return ans