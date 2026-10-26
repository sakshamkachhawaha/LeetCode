class Solution:
    def minFlips(self, target: str) -> int:
        cnt = 0
        cur = '0'
        for i in range(len(target)):
            if target[i]!=cur:
                cnt+=1
                cur = target[i]
        return cnt