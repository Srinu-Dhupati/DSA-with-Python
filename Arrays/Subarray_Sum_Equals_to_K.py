class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        prefix_map={0:1}
        for i in nums:
            prefix+=i
            if prefix-k in prefix_map:
                count+=prefix_map[prefix-k]
            prefix_map[prefix]=prefix_map.get(prefix,0)+1
        return count
