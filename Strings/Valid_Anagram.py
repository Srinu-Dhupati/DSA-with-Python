class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici={}
        dici2={}
        for i in s:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]=dici[i]+1
        for j in t:
            if j not in dici2:
                dici2[j]=1
            else:
                dici2[j]=dici2[j]+1
        if dici==dici2:
            return True
        else:
            return False