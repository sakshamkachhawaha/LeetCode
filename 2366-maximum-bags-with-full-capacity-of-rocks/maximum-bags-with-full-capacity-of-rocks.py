class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        new = []
        for i in range(len(capacity)):
            new.append(capacity[i]-rocks[i])
        new.sort()
        i=0
        cnt = 0
        while i<len(new):
            if additionalRocks-new[i]>=0:
                additionalRocks-=new[i]
                new[i]=0
                cnt+=1
            else:
                break
            i+=1
        return cnt