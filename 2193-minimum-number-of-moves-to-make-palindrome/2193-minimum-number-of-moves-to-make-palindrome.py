class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        lst = list(s)
        count = 0
        center = -1
        left, right = 0, n-1
        while left<right:
            if lst[left]!=lst[right]:
                k = left+1
                while k<right and lst[k]!=lst[right]:
                    k += 1
                if k==right:
                    center=right #should be center of the odd-lengthed string
                    right -= 1
                    continue
                else:
                    for h in range(k,left,-1):
                        tmp = lst[h-1]
                        lst[h-1] = lst[h]
                        lst[h] = tmp
                        count += 1
            left += 1
            right -= 1
        if center>-1: count += (center-n//2)
        return count