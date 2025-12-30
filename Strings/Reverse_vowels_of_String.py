class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        vowels="AEIOUaeiou"
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] in vowels and s[j] not in vowels:
                j-=1
            elif s[j] in vowels and s[i] not in vowels:
                i+=1 
            else:
                i+=1
                j-=1
        s="".join(s)
        return s
     