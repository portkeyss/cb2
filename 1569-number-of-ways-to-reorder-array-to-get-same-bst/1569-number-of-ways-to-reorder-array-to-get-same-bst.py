class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(arr):
            if len(arr) <= 1: return 1
            left = []
            right = []
            for a in arr[1:]:
                if a < arr[0]:
                    left.append(a)
                else:
                    right.append(a)
            return comb(len(left)+len(right), len(left))*f(left)*f(right)
        
        return (f(nums)-1)%(10**9+7)