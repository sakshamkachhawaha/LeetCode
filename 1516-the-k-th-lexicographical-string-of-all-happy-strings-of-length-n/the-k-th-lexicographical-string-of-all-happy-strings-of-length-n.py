class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def isValid(curr):
            for i in range(len(curr)-1):
                if curr[i]==curr[i+1]:
                    return False
            return True
        arr = []
        curr = []
        def f(i):
            if i==n:
                arr.append(''.join(curr))
                return 
            
            for ch in ['a','b','c']:
                curr.append(ch)
                if isValid(curr):
                    f(i+1)
                curr.pop()
        f(0)
        arr.sort()
        if k>len(arr):
            return ""
        else:
            return arr[k-1]