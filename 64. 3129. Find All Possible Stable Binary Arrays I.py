from functools import cache

class Solution:
    def numberOfStableArrays(self, zeros: int, ones: int, limit: int) -> int:
        
        @cache
        def dfs(zero_left: int, one_left: int, last_digit: int) -> int:
            
            if zero_left == 0:
                return int(last_digit == 1 and one_left <= limit)
            
            if one_left == 0:
                return int(last_digit == 0 and zero_left <= limit)

            if last_digit == 0:
                return (
                    dfs(zero_left - 1, one_left, 0)
                    + dfs(zero_left - 1, one_left, 1)
                    - (0 if zero_left - limit - 1 < 0 else dfs(zero_left - limit - 1, one_left, 1))
                )
            
            return (
                dfs(zero_left, one_left - 1, 0)
                + dfs(zero_left, one_left - 1, 1)
                - (0 if one_left - limit - 1 < 0 else dfs(zero_left, one_left - limit - 1, 0))
            )

        MOD = 10**9 + 7
        result = (dfs(zeros, ones, 0) + dfs(zeros, ones, 1)) % MOD
        
        dfs.cache_clear()
        return result
