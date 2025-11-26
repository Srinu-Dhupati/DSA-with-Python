class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        fresult=0
        while i <j:
            leng=j-i
            m=min(height[i],height[j])
            result=m*leng
            fresult=max(result,fresult)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return fresult