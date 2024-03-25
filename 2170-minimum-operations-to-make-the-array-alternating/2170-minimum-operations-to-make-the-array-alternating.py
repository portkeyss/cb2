class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return 0
        evenCounter = Counter()
        oddCounter = Counter()
        for i in range(n):
            if i%2==0:
                evenCounter[nums[i]]+=1
            else:
                oddCounter[nums[i]]+=1
        A = [[v,k] for k,v in evenCounter.items()]
        B = [[v,k] for k,v in oddCounter.items()]
        A.sort(reverse=True)
        B.sort(reverse=True)
        if A[0][1]!=B[0][1]:
            return n-A[0][0]-B[0][0]
        else:
            return min(n-A[0][0]-B[1][0] if len(B)>1 else n-A[0][0], n-B[0][0]-A[1][0] if len(A)>1 else n-B[0][0])