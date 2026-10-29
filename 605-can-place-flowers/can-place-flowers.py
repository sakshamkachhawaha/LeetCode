class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            n-=1
        prev = 0
        for i in range(len(flowerbed)-1):
            if flowerbed[i]==0 and prev == 0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            prev = flowerbed[i]
        
        if prev == 0 and flowerbed[-1]==0:
            n-=1
        if n>0:
            return False
        return True