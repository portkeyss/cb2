class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = 0
        b = 0
        ops1 = 0
        ops2 = 0
        prev = None
        for c in colors:
            if c==prev:
                if c=="A": a += 1
                else: b += 1
            else:
                if a>2: ops1 += a-2
                elif b>2: ops2 += b-2
                a = 0
                b = 0
                if c=="A":
                    a += 1
                else:
                    b += 1
            prev = c
        if a>2: ops1 += a-2
        elif b>2: ops2 += b-2
        return ops1>ops2        