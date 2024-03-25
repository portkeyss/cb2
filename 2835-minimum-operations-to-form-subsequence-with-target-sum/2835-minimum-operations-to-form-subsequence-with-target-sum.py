class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums)<target: return -1
        A = [0]*32
        for x in nums:
            for bit in range(31):
                if (1<<bit)==x:
                    A[bit] += 1
        ans = 0
        missingBit = -1
        for bit in range(31):
            if (1<<bit)&target:
                if A[bit]:
                    A[bit] -= 1
                else:
                    if missingBit<0: missingBit = bit
            if A[bit] and missingBit>=0:
                A[bit] -= 1
                ans += bit - missingBit
                missingBit = -1
            A[bit+1] += A[bit]//2
        return ans