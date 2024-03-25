class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        A = []
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                A.append(nums[i])
        res = 0
        for i in range(1,len(A)-1):
            if A[i-1]<A[i] and A[i+1]<A[i] or A[i-1]>A[i] and A[i+1]>A[i]:
                res += 1
        return res