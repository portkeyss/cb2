class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        bins = batteries[-n:]
        extra = sum(batteries[:-n])
        prefix = 0
        for i,x in enumerate(bins):
            prefix += x
            if i+1<n and extra+prefix<bins[i+1]*(i+1):
                return (extra+prefix)//(i+1)
        return (extra+prefix)//n