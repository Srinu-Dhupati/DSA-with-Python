class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dici={}
        dici2={}
        for i in ransomNote:
            if i  not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for j in magazine:
            if j not in dici2:
                dici2[j]=1
            else:
                dici2[j]+=1
        for ch in ransomNote:
            if ch not in dici2 or dici[ch]>dici2[ch]:
                return False
        return True