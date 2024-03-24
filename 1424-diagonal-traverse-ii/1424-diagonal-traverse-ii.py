class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        A = defaultdict(list)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums[i])):
                A[i+j].append(nums[i][j])
        res = []
        k = 0
        while k in A:
            res += A[k]
            k+=1
        return res