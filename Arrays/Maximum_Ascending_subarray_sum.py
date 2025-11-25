class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        q=1
        sum1=nums[q-1]
        max_sum=sum1
        while q<len(nums):
            if nums[q-1]<nums[q]:
                sum1+=nums[q]
            else:
                sum1=nums[q]
            max_sum=max(max_sum,sum1)
            q+=1

        return max_sum