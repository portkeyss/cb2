class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        mi = mx = 0
        for i,c in enumerate(s):
            if locked[i]=="0":
                mi -= 1
                if mi<0: mi += 2
                mx += 1
            else:
                x = 1 if c=="(" else -1
                mi += x
                mx += x
                if mi<0:
                    if mx>mi:
                        mi += 2
                    else:
                        return False
        return mi==0