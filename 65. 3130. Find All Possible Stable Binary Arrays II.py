class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        @cache
        def dfs(zeros_left, ones_left, place_zero):
            if zeros_left == 0:
                return int(not place_zero and ones_left <= limit)
            if ones_left == 0:
                return int(place_zero and zeros_left <= limit)
            if place_zero:
                return (
                    dfs(zeros_left - 1, ones_left, True)
                    + dfs(zeros_left - 1, ones_left, False)
                    - (0 if zeros_left <= limit else dfs(zeros_left - limit - 1, ones_left, False))
                )
            return (
                dfs(zeros_left, ones_left - 1, True)
                + dfs(zeros_left, ones_left - 1, False)
                - (0 if ones_left <= limit else dfs(zeros_left, ones_left - limit - 1, True))
            )

        mod = 10**9 + 7
        ans = (dfs(zero, one, True) + dfs(zero, one, False)) % mod
        dfs.cache_clear()
        return ans
