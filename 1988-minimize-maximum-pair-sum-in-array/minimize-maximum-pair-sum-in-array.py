class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        mx = 0
        i = 0 
        j = len(nums)-1
        while j>i:
            s = nums[i]+nums[j]
            if s>mx:
                mx = s
            j-=1
            i+=1
        return mx