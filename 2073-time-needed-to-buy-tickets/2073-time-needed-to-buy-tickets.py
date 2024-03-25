class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        nxt = dict()
        prv = dict()
        n = len(tickets)
        for i in range(n-1):
            nxt[i] = i+1
            prv[i+1] = i
        nxt[n-1] = 0
        prv[0] = n-1
        t = 0
        i = 0
        while True:
            tickets[i]-=1
            t += 1
            nextPerson = nxt[i]
            if tickets[i]==0:
                if i==k: return t
                else:
                    a, b = prv[i], nxt[i]
                    nxt.pop(i)
                    prv.pop(i)
                    nxt[a] = b
                    prv[b] = a
                    i = b
            i = nextPerson          
        return t