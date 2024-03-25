class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        mx = -inf
        stack = []
        for num in nums:
            while stack and stack[-1]>num:
                stack.pop()
            if num>mx: stack.append(num)
            mx = max(mx, num)
        return len(stack)