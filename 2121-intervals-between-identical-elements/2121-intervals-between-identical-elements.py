class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        A = [0]*n
        
        dist = Counter()
        prev = dict()
        count = Counter()
        for i,x in enumerate(arr):
            if x in prev:
                dist[x] += count[x]*(i-prev[x])
                A[i] = dist[x]
            count[x] += 1
            prev[x] = i
        
        dist = Counter()
        prev = dict()
        count = Counter()
        for i in range(n-1,-1,-1):
            x = arr[i]
            if x in prev:
                dist[x] += count[x]*(prev[x]-i)
                A[i] += dist[x]
            count[x] += 1
            prev[x] = i
        return A