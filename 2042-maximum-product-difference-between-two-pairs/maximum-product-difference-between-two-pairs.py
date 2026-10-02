class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mx1 = 0
        mx2 = 0
        mi1 = float("+inf")
        mi2 = float("+inf")

        for i in range(len(nums)):
            if nums[i] > mx1:
                mx2 = mx1
                mx1 = nums[i]

            elif nums[i] > mx2 :
                mx2 = nums[i]

            if nums[i] < mi1:
                mi2 = mi1
                mi1 = nums[i]

            elif nums[i] < mi2 :
                mi2 = nums[i]

        return (mx1 * mx2) - (mi1 * mi2)
