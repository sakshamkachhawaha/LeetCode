class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        arr = []
        dic = {}
        cnt = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
            cnt+=1
            if dic.items() <= freq.items():
                arr.append(cnt)
                cnt = 0
        return arr