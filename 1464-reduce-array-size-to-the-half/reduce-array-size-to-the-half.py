class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        new = sorted(freq, key=freq.get, reverse=True)

        total = len(arr)

        cnt = 0
        for n in new:
            total -= freq[n]
            cnt += 1
            if total <= len(arr)//2:
                return cnt
