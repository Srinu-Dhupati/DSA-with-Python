class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter as c
        l1=[]
        p_counter=c(p)
        window_counter=c()
        for i,ch in enumerate(s):
            window_counter[ch]+=1
            if i>=len(p):
                window_counter[s[i-len(p)]]-=1
                if window_counter[s[i-len(p)]]==0:
                    del window_counter[s[i-len(p)]]
            if window_counter==p_counter:
                l1+=[i-len(p)+1]
        return l1