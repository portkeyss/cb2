class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        res = inf
        for x in "abcdefghijklmnopqrstuvwxy":#x is the upper bound for lower string, note that letter z is absent because it is not applicable
            ops1, ops2 = 0, 0
            for p in a:
                if p>x: #how many operations is needed to make p<=x
                    ops1 += 1
                else: #how many operations is need to make p>x
                    ops2 += 1
            for q in b:
                if q<=x: #how many operations is needed to make q>x
                    ops1 += 1
                else:##how many operations is needed to make p<=x
                    ops2 += 1
            res = min(res, ops1, ops2)
        count1 = Counter(a)
        count2 = Counter(b)
        res = min(res, len(a)-max(count1.values())+len(b)-max(count2.values()))
        return res