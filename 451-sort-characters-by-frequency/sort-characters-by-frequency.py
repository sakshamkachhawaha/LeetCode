class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1

        sorted_freq = sorted(freq, key = freq.get ,reverse = True)
        ans = ""
        for c in sorted_freq:
            ans+=c * freq[c]
        
        return ans