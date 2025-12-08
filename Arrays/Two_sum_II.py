class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            v=numbers[i]+numbers[j]
            if v==target:
                return(i+1,j+1)
            elif v<target:
                i+=1
            else:
                j-=1