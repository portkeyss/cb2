class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors1 = []
        divisors2 = []
        for i in range(1, floor(sqrt(n))+1):
            if n % i == 0:
                divisors1.append(i)
                divisors2.append(n//i)
        divisors = divisors1+ (divisors2[-2::-1] if divisors1[-1] == divisors2[-1] else divisors2[::-1])
        return divisors[k-1] if len(divisors) >= k else -1