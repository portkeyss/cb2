class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        A = defaultdict(lambda:0)
        for a,b in lights:
            A[a-b] += 1
            A[a+b+1] -= 1
        balance = 0
        mx = 0
        ps = None
        for p in sorted(A.keys()):
            balance += A[p]
            if balance > mx:
                mx = balance
                ps = p
        return ps