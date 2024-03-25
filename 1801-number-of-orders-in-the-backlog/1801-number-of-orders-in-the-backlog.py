class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyOrders = []
        sellOrders = []
        for price,amount,orderType in orders:
            if orderType ==0:
                n = amount
                while n>0 and sellOrders and sellOrders[0][0] <= price:
                    if n >= sellOrders[0][1]:
                        n -= sellOrders[0][1]
                        heapq.heappop(sellOrders)
                    else:
                        pr,amt = heapq.heappop(sellOrders)
                        heapq.heappush(sellOrders, (pr,amt-n))
                        n = 0 
                if n > 0:
                    heapq.heappush(buyOrders, (-price, n))
            else:
                n = amount
                while n>0 and buyOrders and -buyOrders[0][0] >= price:
                    if n >= buyOrders[0][1]:
                        n -= buyOrders[0][1]
                        heapq.heappop(buyOrders)
                    else:
                        negPr,amt = heapq.heappop(buyOrders)
                        heapq.heappush(buyOrders, (negPr,amt-n))
                        n = 0 
                if n > 0:
                    heapq.heappush(sellOrders, (price, n))
        return (sum(amt for _,amt in buyOrders) + sum(amt for _,amt in sellOrders))%(10**9+7)