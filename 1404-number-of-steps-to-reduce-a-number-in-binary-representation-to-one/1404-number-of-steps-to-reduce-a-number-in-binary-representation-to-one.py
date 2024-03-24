class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for c in s:
            num = (num<<1)+int(c)
        steps = 0
        while num!=1:
            if num%2==0:
                num >>= 1
            else:
                num += 1
            steps += 1
        return steps