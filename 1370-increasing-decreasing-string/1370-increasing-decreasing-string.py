class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        direction = 1
        A = "abcdefghijklmnopqrstuvwxyz"
        buffer = []
        while counter:
            ite = A if direction==1 else reversed(A)
            for x in ite:
                if x in counter:
                    buffer.append(x)
                    counter[x] -= 1
                    if counter[x]==0: counter.pop(x)
            direction*=-1
        return "".join(buffer)