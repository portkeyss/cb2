class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        flips = 0
        for c in target:
            if c=="0" and flips%2==1 or c=="1" and flips%2==0: flips += 1
        return flips