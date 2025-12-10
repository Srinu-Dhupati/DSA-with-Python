class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        min_length=len(nums)+1
        sum1=0
        for j in range(0,len(nums)):
            sum1+=nums[j]
            while sum1>=target:
                min_length=min(min_length,j-i+1)
                sum1-=nums[i]
                i+=1
        return min_length if min_length!=len(nums)+1 else 0