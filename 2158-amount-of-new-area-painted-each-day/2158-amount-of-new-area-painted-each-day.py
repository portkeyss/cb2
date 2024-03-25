class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        jump = dict()
        res = []
        for s,e in paint:
            x = 0
            nxt = None
            while s<e:
                if s in jump:
                    nxt = jump[s]
                    jump[s] = max(jump[s], e)
                else:
                    x += 1
                    jump[s] = e
                    nxt = s+1
                s = nxt
            res.append(x)
        return res