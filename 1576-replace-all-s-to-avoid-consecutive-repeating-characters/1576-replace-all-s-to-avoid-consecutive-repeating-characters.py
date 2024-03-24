class Solution:
    def modifyString(self, s: str) -> str:
        buffer = []
        for i in range(len(s)):
            if s[i] != "?":
                buffer.append(s[i])
            else:
                candidates = set(("a", "b", "c"))
                if i-1 >= 0:
                    candidates.discard(buffer[i-1])
                if i+1 < len(s):
                    candidates.discard(s[i+1])
                buffer.append(candidates.pop())
        return "".join(buffer)