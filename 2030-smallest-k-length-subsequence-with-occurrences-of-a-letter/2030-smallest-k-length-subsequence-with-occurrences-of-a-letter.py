class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        count = list(accumulate(c==letter for c in s[::-1]))[::-1]
        stack = []
        for i,c in enumerate(s):
            while stack and stack[-1]>c and n-i>=k+1 and (stack[-1]!=letter or count[i]>=repetition+1):
                a = stack.pop()
                repetition += a==letter
                k += 1
            if k>0 and (c==letter or k>repetition):
                stack.append(c)
                repetition -= c==letter
                k -= 1
        return "".join(stack)