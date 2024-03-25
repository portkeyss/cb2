class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = N//2
        tot = sum(nums)
        leftSums = [set() for _ in range(n+1)]
        leftSums[0] = set([0])
        rightSums = [set() for _ in range(n+1)]
        rightSums[0] = set([0])
        def f(arr, A):
            for i,p in enumerate(arr):
                for sz in range(i+1,0,-1):
                    for x in A[sz-1]:
                        A[sz].add(x+p)
        f(nums[:n], leftSums)
        f(nums[n:], rightSums)
        for i in range(n+1):
            rightSums[i] = sorted(list(rightSums[i]))
        res = inf
        for sz in range(n+1):
            for ls in leftSums[sz]:
                idx = bisect.bisect(rightSums[n-sz], tot/2-ls)
                rs1 = rs2 = None
                if idx==0:
                    rs1 = rs2 = rightSums[n-sz][0]
                elif idx==len(rightSums[n-sz]):
                    rs1 = rs2 = rightSums[n-sz][-1]
                else:
                    rs1 = rightSums[n-sz][idx-1]
                    rs2 = rightSums[n-sz][idx]
                res = min(res, abs(tot-2*ls-2*rs1), abs(tot-2*ls-2*rs2))
        return res