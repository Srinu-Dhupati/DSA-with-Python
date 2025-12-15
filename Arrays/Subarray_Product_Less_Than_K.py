class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
        j=0
        product=1
        if k<=1:
            return 0
        for i in range(len(nums)):
            product*=nums[i]
            while product>=k and j<=i:
                product//=nums[j]
                j+=1
            count+=i-j+1
        return count
