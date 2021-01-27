class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s != '0' else 0
        array = [0] * (n + 1)
        array[0] = 1
        for i in range(1, n+1):
            if '1' <= s[i-1] <= '9':
                array[i] += array[i-1]
            if '10' <= s[i-2:i] <= '26':
                array[i] += array[i-2]
        return array[n]
