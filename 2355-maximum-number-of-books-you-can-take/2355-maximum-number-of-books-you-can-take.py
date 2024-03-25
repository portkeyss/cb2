class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        stack = [] # monotonic increasing stack with height difference btw neighbors>their index position difference
        res = 0
        for i,b in enumerate(books):
            while stack and books[stack[-1][0]]>=b-(i-stack[-1][0]):
                stack.pop()
            j = stack[-1][0]+1 if stack else 0
            base = stack[-1][1] if stack else 0
            low, high = max(0,b-i+j),b
            x = base+(low+high)*(high-low+1)//2
            stack.append((i,x))
            res = max(res,x)
        return res