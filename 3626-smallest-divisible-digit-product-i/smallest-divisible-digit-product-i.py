class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def f(n):
            temp=1
            while n>0:
                temp*=n%10
                n//=10
            return temp

        for i in range(t):
            if f(n)%t==0:
                return n
            else:
                n+=1