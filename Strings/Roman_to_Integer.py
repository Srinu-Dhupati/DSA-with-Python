class Solution:
    def romanToInt(self, s: str) -> int:
        li=[]
        sum1=0
        for i in s:
            if i=="I":
                li+=[1]
            elif i=="V":
                li+=[5]
            elif i=="X":
                li+=[10]
            elif i=="L":
                li+=[50]
            elif i=="C":
                li+=[100]
            elif i=="D":
                li+=[500]
            else:
                li+=[1000]
        j=0
        while j<=len(li)-2:
                if li[j]<li[j+1]:
                    sum1+=(li[j+1]-li[j])
                    j+=2
                else:
                    sum1+=li[j]
                    j+=1
        li2=li.copy()
        li2.sort(reverse=True)
        if li==li2:
            sum1+=li[-1]
        
        else:
            if j==len(li)-1:
                sum1+=li[j]
        return sum1

                    