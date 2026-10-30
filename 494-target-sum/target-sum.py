class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        if (sum(nums)+target) %2!=0 or sum(nums) < abs(target):
            return 0

        k = (sum(nums)+target)//2
        dp = [[-1]*(k+1) for _ in range(len(nums))]
        def f(i,k):
            if i==len(nums):
                if k==0:
                    return 1
                return 0
            
            if dp[i][k]!=-1:
                return dp[i][k]
            exclude = f(i+1,k)
            include = 0
            if k>=nums[i]:
                include = f(i+1,k - nums[i])
            dp[i][k] = include + exclude
            return dp[i][k]
        return f(0,k)