class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        A = [] #A is the unique numbers sorted
        for num in range(100001):
            if num in counter: A.append(num)
        prefix = [0]
        for a in A:
            prefix.append(prefix[-1]+counter[a])
        res = counter[A[0]]
        i = 0
        ops = 0
        for j in range(1,len(prefix)-1):
            ops += (A[j]- A[j-1])*(prefix[j]-prefix[i])
            while ops > k:
                ops -= (A[j]-A[i])*counter[A[i]]
                i += 1
            freq = prefix[j+1]-prefix[i]
            if i > 0:
                freq += (k-ops)//(A[j]-A[i-1])
            res = max(res, freq)
        return res