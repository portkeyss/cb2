# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        left = 0
        right = binaryMatrix.dimensions()[1] - 1
        while left < right:
            mid = left + (right - left)/2
            if self.oneInColumn(binaryMatrix, mid):
                right = mid
            else:
                left = mid + 1
        return left if self.oneInColumn(binaryMatrix, left) else -1
    
    def oneInColumn(self, binaryMatrix, col):
        for i in range(binaryMatrix.dimensions()[0]):
            if binaryMatrix.get(i, col) == 1:
                return True
        return False
     