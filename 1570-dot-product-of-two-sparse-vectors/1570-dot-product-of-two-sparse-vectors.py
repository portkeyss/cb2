class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        "create a dictionary to map nonezero valued index to value"
        self.val = {i: x for i, x in enumerate(nums)}
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        "iterate thru the dict of self.val and multiply elementwise with the corresponding value with the same indices, if not exist, default to zero, finally do a sum"
        return sum(vec.val.get(i,0) * x for i, x in self.val.items())
        
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)