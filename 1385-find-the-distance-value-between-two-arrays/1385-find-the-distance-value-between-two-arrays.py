class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        if d==0:
            arr2=set(arr2)
            return sum(a not in arr2 for a in arr1)
        ends = Counter()
        arr2 = list(set(arr2))
        for b in arr2:
            ends[b-d] += 1
            ends[b+d] -= 1
        mi = min(ends.keys())
        mx = max(ends.keys())
        balance = 0
        points = []
        for i in range(mi, mx+1):
            if balance == 0 and ends[i]==1 or balance == 1 and ends[i]==-1:
                points.append(i)
            balance += ends[i]
        ans = 0
        for a in arr1:
            j = bisect.bisect_left(points,a)
            if j==len(points) or (j%2==0 and points[j]>a):
                ans += 1
        return ans