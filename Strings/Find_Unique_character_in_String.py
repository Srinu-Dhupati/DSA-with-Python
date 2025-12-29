class Solution:
    def firstUniqChar(self, s: str) -> int:
        dici={}
        count=0
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for i in dici:
            if dici[i]==1:
                return s.index(i)
        else:
            return -1