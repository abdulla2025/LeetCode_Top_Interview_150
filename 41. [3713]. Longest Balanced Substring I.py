class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        result = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                counts = set(freq.values())
                if len(counts) == 1:
                    result = max(result, j - i + 1)
        return result
