class Solution:
    def minOperations(self, s: str) -> int:
        zero = one = 0
        for c in s:
            z = o = 0
            if c == "0":
                z = one
                o = zero + 1
            else:
                z = one + 1
                o = zero
            zero, one = z, o
        return min(zero, one)