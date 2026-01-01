class Solution:
    def intToRoman(self, num: int) -> str:
        dici={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
        dici3={1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"}
        dici2={1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"}
        dici4={1:"M",2:"MM",3:"MMM"}
        r=0
        temp=num
        count=0
        roman=""
        while temp>0:
            r=temp%10
            temp//=10
            count+=1
            if count==1:
                if r==0:
                    continue
                else:
                    roman+=str(dici[r])
            elif count==2:
                if r==0:
                    continue
                else:
                    roman=str(dici2[r])+roman
            elif count==3:
                if r==0:
                    continue
                else:
                    roman=str(dici3[r])+roman
            else:
                roman=str(dici4[r])+roman
        return roman