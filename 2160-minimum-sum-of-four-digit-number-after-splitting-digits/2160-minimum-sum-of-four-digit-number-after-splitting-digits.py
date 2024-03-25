class Solution:
    def minimumSum(self, num: int) -> int:
        l = [x for x in str(num)]
        res = inf
        for mask in range(1,(1<<4)-1):
            A = []
            B = []
            for b in range(4):
                if (1<<b)&mask:
                    A.append(l[b])
                else:
                    B.append(l[b])
            res = min(res, int("".join(sorted(A)))+int("".join(sorted(B))))
        return res