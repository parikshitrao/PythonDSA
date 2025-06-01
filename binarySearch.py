class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        u=len(nums)-1
        if nums[l] == target:
            return l
        elif nums[u] == target:
            return u
        while l<=u:
            mid = (l+u)//2 
            if nums[mid] > target:
                u = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1