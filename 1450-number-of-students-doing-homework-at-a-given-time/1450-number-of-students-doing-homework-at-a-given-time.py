class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        A = Counter()
        for s,e in zip(startTime,endTime):
            A[s] += 1
            A[e+1] -= 1
        timestamps = sorted(list(A.keys()))
        balance = 0
        B = []
        for ts in timestamps:
            balance += A[ts]
            B.append([ts, balance])
        i = bisect.bisect(B,[queryTime,inf])-1
        return B[i][1] if i>=0 else 0