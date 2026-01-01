class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dici={}
        for index,i in enumerate(strs):
            i="".join(sorted(i))
            if i not in dici:
                dici[i]=[strs[index]]
            else:
                dici[i]=dici[i]+[strs[index]]
        return list(dici.values())