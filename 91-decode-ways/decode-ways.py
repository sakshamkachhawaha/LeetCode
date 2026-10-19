class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = [-1]*(n+1)
        def f(i):
            if i==n:
                return 1
            if memo[i]!=-1:
                return memo[i]
            ways = 0
            if s[i]!='0':
                ways+=f(i+1)
            if i+1<n and '10'<=s[i:i+2]<='26':
                ways+=f(i+2)
            memo[i]=ways
            return ways
        return f(0)