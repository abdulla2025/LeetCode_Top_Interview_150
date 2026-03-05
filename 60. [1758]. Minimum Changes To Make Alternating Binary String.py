class Solution:
    def minOperations(self, s: str) -> int:
        cost_a = 0
        cost_b = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '1':
                    cost_a += 1
                else:
                    cost_b += 1
            else:
                if s[i] == '0':
                    cost_a += 1
                else:
                    cost_b += 1
        return min(cost_a, cost_b)
