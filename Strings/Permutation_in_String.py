class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter as c
        s1_counter=c(s1)
        window_counter=c()
        for i,ch in enumerate(s2):
            window_counter[ch]+=1
            if i>=len(s1):
                window_counter[s2[i-len(s1)]]-=1
                if window_counter[s2[i-len(s1)]]==0:
                    del window_counter[s2[i-len(s1)]]
            if window_counter==s1_counter:
                return True
        else:
            return False