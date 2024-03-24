class Solution:
    def countLargestGroup(self, n: int) -> int:
        A = Counter()
        for i in range(1,n+1):
            A[sum(int(c) for c in str(i))] += 1
        m = max(A.values())
        return sum(v==m for v in A.values())