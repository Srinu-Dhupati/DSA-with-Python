class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dici={}
        for index,values in enumerate(nums):
            two_sum=target-values
            if two_sum in dici:
                return (dici[two_sum],index)
            dici[values]=index
