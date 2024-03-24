class Solution:
    def average(self, salary: List[int]) -> float:
        mi = inf
        mx = -inf
        sm = 0
        for s in salary:
            mi=min(mi,s)
            mx=max(mx,s)
            sm += s
        return (sm-mi-mx)/(len(salary)-2)