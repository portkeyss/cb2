class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and (c.isupper() and c.lower()==stack[-1] or c.islower() and c.upper()==stack[-1]):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)