class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        mx=0
        for i in range(len(s)):
            dic={}
            l=0
            for j in range(i,len(s)):
                if dic.get(s[j], 0) == 2:
                    break
                
                dic[s[j]] = dic.get(s[j], 0) + 1
                l+=1
                if mx<l:
                    mx=l
        return mx