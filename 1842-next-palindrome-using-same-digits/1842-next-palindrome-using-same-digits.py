class Solution:
    def nextPalindrome(self, num: str) -> str:
        n = len(num)
        if n==1: return ""
        A = list(num[:n//2])

        def nextPerm(lst):
            m = len(lst)
            p = m-2
            while p>=0 and lst[p]>=lst[p+1]:
                p -= 1
            if p==-1: return []
            q = m-1
            while lst[p]>=lst[q]:
                q -= 1
            lst[p], lst[q] = lst[q], lst[p]
            l, r = p+1,m-1
            while l<r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
            return lst
                
        B = nextPerm(A)
        if B==[]: return ""
        mid = "" if n%2==0 else num[n//2]
        return "".join(B+[mid]+B[::-1])