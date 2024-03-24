class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        mid = -1
        if n % 2 == 1:
            mid = n // 2
        i = 0
        while i < len(palindrome):
            if i != mid and palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            i += 1
        i -= 1
        if i >= 0 and i != mid:
            return palindrome[:i] +'b'
        return ""