class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=""
        for i in digits:
            n+=str(i)
        n=(int(n)+1)
        nums=[]
        for i in str(n):
            nums+=[int(i)]
        return nums