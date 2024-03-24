from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        placeholder = 10**9
        res = []
        full = dict()
        availables = SortedList()
        for i in range(n):
            if rains[i]==0:
                res.append(placeholder)
                availables.add(i)
            else:
                if rains[i] in full:
                    j = availables.bisect(full[rains[i]])
                    if j==len(availables): return []
                    res[availables[j]] = rains[i]
                    availables.remove(availables[j])
                full[rains[i]] = i
                res.append(-1)
        return res