class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l3=nums1[:m]
        i,j,k=0,0,0
        while i<len(l3) and j<n:
            if l3[i]>nums2[j]:
                nums1[k]=nums2[j]
                j+=1
            else:
                nums1[k]=l3[i]
                i+=1

            k+=1
        while i <len(l3):
            nums1[k]=l3[i]
            i+=1
            k+=1
        while j<n:
            nums1[k]=nums2[j]
            j+=1
            k+=1
        return nums1 