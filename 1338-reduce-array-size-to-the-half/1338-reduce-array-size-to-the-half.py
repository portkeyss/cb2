class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        A = sorted(list(counter.values()),reverse=True)
        p = 0
        for i,x in enumerate(A):
            p += x
            if p>=(1+len(arr))//2: return i+1