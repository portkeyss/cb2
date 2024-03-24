# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def fit(f,x):
            return sum(fontInfo.getWidth(f,ch) for ch in text)<=w and fontInfo.getHeight(f)<=h
        if fit(fonts[0],text) is False: return -1
        l, r = 0, len(fonts)-1
        while l<r:
            m = (l+r+1)//2
            if fit(fonts[m],text):
                l=m
            else:
                r=m-1
        return fonts[r]