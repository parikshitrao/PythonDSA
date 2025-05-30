class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: 
                    return[i,j]

        # most optimal solutions using hash map - dictionary  
        # seen = {}        
        # for i, num in enumerate(nums):
        #     compliment = target - nums
        #     if compliment in seen:
        #         return [seen[compliment], i]
        #     seen[nums] = i