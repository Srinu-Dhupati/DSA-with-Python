class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l1=[]
        set1=[]
        for i in nums:
            if i not in l1:
                l1+=[i]
            else:
                set1+=[i]
        nums=[*{*nums}]
        for j in set1:
            nums.remove(j)
        return nums[0]
         