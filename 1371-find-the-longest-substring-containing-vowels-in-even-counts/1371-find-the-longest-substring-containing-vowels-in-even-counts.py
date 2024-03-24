class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        vowels = {ch:i for i,ch in enumerate("aeiou")}
        mask2idx = {0:-1}
        ans = 0
        for i,c in enumerate(s):
            if c in vowels:
                mask ^= 1<<vowels[c]
            if mask in mask2idx:
                ans = max(ans,i-mask2idx[mask])
            else:
                mask2idx[mask] = i
        return ans