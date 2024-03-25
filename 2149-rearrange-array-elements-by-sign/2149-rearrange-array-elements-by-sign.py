class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        i,j = 0,1
        for num in nums:
            if num>0:
                arr[i]=num
                i += 2
            else:
                arr[j]=num
                j += 2
        return arr