class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2==1: return []
        i = 2
        sm = 0
        res = []
        while sm<finalSum:
            sm += i
            res.append(i)
            i += 2
        if sm==finalSum: return res
        x = res.pop()
        res[-1] += finalSum-(sm-x)
        return res