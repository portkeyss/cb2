class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(s)
        m = len(part)
        part=list(part)
        for c in s:
            stack.append(c)
            if len(stack)>=m and stack[-m:]==part: stack[-m:]=[]
        return "".join(stack)