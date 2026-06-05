class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def solve_for_num(num):
            if num < 100:
                return 0
            
            s = str(num)
            n = len(s)
            
            from functools import lru_cache
            
            @lru_cache(None)
            def dp(pos, prev_prev, prev, is_limited, is_leading_zero):
                if pos == n:
                    return (1, 0)
                
                limit = int(s[pos]) if is_limited else 9
                total_numbers = 0
                total_waviness = 0
                
                for dig in range(limit + 1):
                    new_is_leading_zero = is_leading_zero and (dig == 0)
                    new_prev_prev = prev
                    new_prev = -1 if new_is_leading_zero else dig
                    
                    rem_numbers, rem_waviness = dp(
                        pos + 1, new_prev_prev, new_prev,
                        is_limited and (dig == limit),
                        new_is_leading_zero
                    )
                    
                    if not new_is_leading_zero and prev_prev >= 0 and prev >= 0:
                        is_peak = (prev_prev < prev and prev > dig)
                        is_valley = (prev_prev > prev and prev < dig)
                        if is_peak or is_valley:
                            total_waviness += rem_numbers
                    
                    total_numbers += rem_numbers
                    total_waviness += rem_waviness
                
                return (total_numbers, total_waviness)
            
            return dp(0, -1, -1, True, True)[1]
        
        return solve_for_num(num2) - solve_for_num(num1 - 1)
