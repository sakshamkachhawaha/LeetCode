class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        reach = 0
        for i in range(len(nums)):
            if i==reach and nums[i]==0 and i<len(nums)-1:
                return False
            if reach >= len(nums)-1:
                return True
            if nums[i]+i>reach:
                reach = i+nums[i]

        return False