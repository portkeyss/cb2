class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1]*n
        stack = [n-1]
        for i in range(n-2,-1,-1):
            while stack and ((cars[i][1]-cars[stack[-1]][1]) <= 0 or (cars[stack[-1]][0] - cars[i][0])/(cars[i][1]-cars[stack[-1]][1]) > ans[stack[-1]] > 0):
                stack.pop()
            if stack and (cars[i][1]-cars[stack[-1]][1]) > 0:
                ans[i] = (cars[stack[-1]][0] - cars[i][0])/(cars[i][1]-cars[stack[-1]][1])
            stack.append(i)
        return ans