class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        dq = deque()
        dq.append((-1,0,0))
        prefix = 0
        portChange = 0
        prevPort = -1
        #monotonic deque
        for i,(p,w) in enumerate(boxes):
            prefix += w
            portChange += (p!=prevPort)
            prevPort = p
            while dq[0][0]<i-maxBoxes or dq[0][1]<prefix-maxWeight: dq.popleft()
            oldTrips = dq[0][2]
            trips = oldTrips
            if i==len(boxes)-1:
                return oldTrips+portChange+1
            if p==boxes[i+1][0]: trips += 2
            else:trips += 1
            while dq[-1][2]>=trips: dq.pop()
            dq.append((i,prefix,trips))