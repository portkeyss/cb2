class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(b) for b in boxes]
        n = len(boxes)
        prefix = boxes[0]
        rightMoves = [0]*n
        for i in range(1,n):
            rightMoves[i] = prefix+rightMoves[i-1]
            prefix += boxes[i]
        postfix = boxes[n-1]
        leftMoves = [0]*n
        for i in range(n-2,-1,-1):
            leftMoves[i] = postfix+leftMoves[i+1]
            postfix += boxes[i]
        return [r+l for r,l in zip(rightMoves, leftMoves)]