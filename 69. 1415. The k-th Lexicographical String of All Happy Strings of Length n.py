class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2 ** (n - 1)):
            return ""
        result = []
        k -= 1
        for i in range(n):
            branch_size = 2 ** (n - i - 1)
            for c in ['a', 'b', 'c']:
                if result and result[-1] == c:
                    continue
                if k < branch_size:
                    result.append(c)
                    break
                k -= branch_size
        return "".join(result)
