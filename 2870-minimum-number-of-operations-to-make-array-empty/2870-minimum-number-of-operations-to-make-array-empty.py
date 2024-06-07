class Solution:
    def minOperations(self, nums: List[int]) -> int:
        A = Counter(nums).values()
        if 1 in A: return -1
        res = 0
        for a in A:
            if a%3==0: res += a//3
            elif a%3==1: res += (a-3)//3+2
            else: res += a//3+1
        return res