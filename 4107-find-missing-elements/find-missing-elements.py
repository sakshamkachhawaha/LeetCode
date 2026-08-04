class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        lst=[]
        for i in range(a,b+1):
            if i not in nums:
                lst.append(i)
        return lst