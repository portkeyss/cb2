class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        counter = Counter(inventory)
        A = [[0,0]]
        A.extend(list(sorted([h,ct] for h,ct in counter.items())))
        res = 0
        while len(A) > 1:
            h1, h2 = A[-1][0], A[-2][0]
            width = A[-1][1]
            c = (h1 - h2)*width
            if c < orders:
                A[-2][1] += width
                A.pop()
                orders -= c
                res += width*(h2+1+h1)*(h1-h2)//2
            else:
                m = orders % width
                n = orders // width
                res += width*(2*h1-n+1)*n//2 + m*(h1-n)
                return res % (10**9+7)