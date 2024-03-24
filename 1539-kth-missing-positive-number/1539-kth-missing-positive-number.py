class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        "create an array with size 2000, by default, every value has value 0, then we iterate thru the original array, we mark a[arr[i]] = 1, then we iterate thru a, find kth zero location, and return this index"
        "what should the size of a be? we know that the arr takes value from 1 to 1000, and k from 1 to 1000, therefore a can go beyond size 1000. But what is the max possibe value for a's size? The lastest possible start position for missing value is 1001, and largest k is 1000, therefore size of a should be set as 2000 "
        a = [0]*2001
        for num in arr:
            a[num] = 1 
        m = 0
        for j in range(1,2001):
            if a[j] == 0:
                m += 1
                if m == k:
                    return j
                
        
            
        
        