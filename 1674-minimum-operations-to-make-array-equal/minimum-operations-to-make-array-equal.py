class Solution:
    def minOperations(self, n: int) -> int:
        
        arr = []
        for i in range(n):
            arr.append(2*i+1)
        
        target = sum(arr)//n
        cnt = 0
        for i in range(n//2):
            cnt+=abs(arr[i]-target)
        return cnt