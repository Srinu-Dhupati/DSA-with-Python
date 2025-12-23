class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1=len(haystack)
        n=len(needle)
        a=[]
        count=0
        for i in range(0,n1-n+1):
            a+=[haystack[i:i+n]]
        if needle in a:
            return haystack.index(needle)
        else:
            return -1