class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        map1={}
        for i in nums2:
            while stack and stack[-1]<i:
                map1[stack.pop()]=i
            stack.append(i)
        return [map1.get(x,-1) for x in nums1]
