class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(2,num+1):
            res += sum(int(c) for c in str(i))%2==0
        return res