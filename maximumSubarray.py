class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current = nums[0] 
        for i in nums[1:]:
            current = max (i, current+i)
            max_sum = max(current, max_sum)

        return max_sum