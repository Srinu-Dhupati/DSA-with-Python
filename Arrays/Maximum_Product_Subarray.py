class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product=nums[0]
        max_product=nums[0]
        result=nums[0]
        for j in range(1,len(nums)):
            if nums[j]<0:
                max_product,min_product=min_product,max_product
            max_product=max(nums[j],max_product*nums[j])
            min_product=min(nums[j],min_product*nums[j])
            result=max(result,max_product)
        return result