class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        l1=[]

        while i<len(nums):
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            else:
                j=i+1
                k=len(nums)-1
                while j<k:
                    cur=nums[i]+nums[j]+nums[k]
                    if cur>0:
                        k-=1
                    elif cur<0:
                        j+=1
                    else:
                        l1+=[[nums[i],nums[j],nums[k]]]
                        j+=1
                        k-=1
                        while j<k and nums[j]==nums[j-1]:
                            j+=1
                        while j<k and nums[k]==nums[k+1]:
                            k-=1
                    
            i+=1
        return l1