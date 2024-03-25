class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        for a,b in adjacentPairs:
            neighbors[a].append(b)
            neighbors[b].append(a)
        res = []
        for a,nei in neighbors.items():
            if len(nei) == 1:
                res.append(a)
                res.append(nei[0])
                break
        while True:
            nei = neighbors[res[-1]]
            if len(nei) == 1:
                return res
            else:
                for a in nei:
                    if a != res[-2]:
                        res.append(a)
                        break