class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        s = [Counter() for _ in range(4)]
        s[0][0] += 1
        res = 0
        for num in nums:
            if s[3] and num in s[3]:
                res += s[3][num]
            for i in range(3,0,-1):
                for p in s[i-1]:
                    s[i][p+num] += s[i-1][p]
        return res