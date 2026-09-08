
class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr = []

        def f(start, s):
            if start == n:
                arr.append(s)
                return

            if s != "" and s[-1] == '0':
                s += '1'
                f(start + 1, s)
                return

            for i in range(0, 2):
                s += str(i)
                f(start + 1, s)
                s = s[:-1]

        f(0, "")

        return arr

