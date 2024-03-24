class Solution:
    def maximum69Number (self, num: int) -> int:
        p = str(num)
        for i,c in enumerate(p):
            if c=="6": return int(p[:i]+"9"+p[i+1:])
        return num