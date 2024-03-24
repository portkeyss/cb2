from sortedcontainers import SortedList
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sl = SortedList()
        smallerPreCount = defaultdict(lambda:0)
        largerPreCount = defaultdict(lambda:0)
        ans = 0
        n = len(rating)
        for j in range(n):
            for i in range(1,j):
                if rating[i] < rating[j]:
                    ans += smallerPreCount[rating[i]]
                else:
                    ans += largerPreCount[rating[i]]
            m = sl.bisect(rating[j])
            smallerPreCount[rating[j]] = m
            largerPreCount[rating[j]] = len(sl)-m
            sl.add(rating[j])
        return ans