class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0]*n
        for i in range(n-1,-1,-1):
            x = 0
            while stack and heights[i]>stack[-1]:
                x += 1
                stack.pop()
            res[i] = x+1 if stack else x
            stack.append(heights[i])
        return res