class NumArray:

    def __init__(self, nums: List[int]):
        j=0
        prefix=0
        while j<len(nums):
            prefix+=nums[j]
            nums[j]=prefix
            j+=1
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
                return self.nums[right]
        else:
                return self.nums[right]-self.nums[left-1]