class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j=0
        sub_ar_sum=nums[j]
        max_sum=sub_ar_sum
        while j<len(nums)-1:
            j+=1
            if sub_ar_sum>=0:
                sub_ar_sum+=nums[j]
            else:
                sub_ar_sum=nums[j]
            max_sum=max(max_sum,sub_ar_sum)

        return max_sum