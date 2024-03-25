class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        stack1 = []
        stack2 = []
        A = [0]*n
        B = [0]*n
        for i in range(n):
            while stack1 and nums[stack1[-1]]>nums[i]:
                stack1.pop()
            A[i] = stack1[-1] if stack1 else -1
            stack1.append(i)
            while stack2 and nums[stack2[-1]]<nums[i]:
                stack2.pop()
            B[i] = stack2[-1] if stack2 else -1
            stack2.append(i)
        stack1 = []
        stack2 = []
        minSum = 0
        maxSum = 0
        for i in range(n-1,-1,-1):
            while stack1 and nums[stack1[-1]]>=nums[i]:
                stack1.pop()
            minSum += nums[i]*(i-A[i])*((stack1[-1] if stack1 else n)-i)
            stack1.append(i)
            while stack2 and nums[stack2[-1]]<=nums[i]:
                stack2.pop()
            maxSum += nums[i]*(i-B[i])*((stack2[-1] if stack2 else n)-i)
            stack2.append(i)
        return maxSum-minSum   