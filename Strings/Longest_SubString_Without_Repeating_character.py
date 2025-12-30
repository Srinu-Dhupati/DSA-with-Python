class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        set1=set()
        m_length=0
        while j<len(s):
            if s[j] not in set1:
                set1.add(s[j])
                m_length=max(m_length,len(set1))
                j+=1
            else:
                set1.discard(s[i])
                i+=1
        return m_length