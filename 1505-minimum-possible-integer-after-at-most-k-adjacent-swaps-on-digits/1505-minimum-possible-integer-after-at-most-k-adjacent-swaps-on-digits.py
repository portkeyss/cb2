from sortedcontainers import SortedList
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        num = [int(ch) for ch in num]
        buffer = []
        n = len(num)
        A = [deque() for _ in range(10)]
        treated = SortedList()
        for i in range(n):
            A[num[i]].append(i)
        i = 0
        while i<n:
            if i in treated: 
                i += 1
                continue
            for d in range(10):
                #while A[d] and A[d][0]<i:
                #    A[d].popleft()
                if A[d]:
                    a = treated.bisect_right(i)
                    b = treated.bisect_right(A[d][0])
                    if A[d][0]-i-(b-a)<=k:
                        j = A[d].popleft()
                        k -= j-i-(b-a)
                        buffer.append(num[j])
                        treated.add(j)
                        break
        return "".join(map(str,buffer))