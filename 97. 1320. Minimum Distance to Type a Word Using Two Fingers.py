class Solution:
    def minimumDistance(self, word: str) -> int:
        from math import inf
        def get_distance(from_key: int, to_key: int) -> int:
            r1, c1 = divmod(from_key, 6)
            r2, c2 = divmod(to_key, 6)
            return abs(r1 - r2) + abs(c1 - c2)
        length = len(word)
        dp = [[[inf] * 26 for _ in range(26)] for _ in range(length)]
        first_char = ord(word[0]) - ord('A')
        for finger_pos in range(26):
            dp[0][first_char][finger_pos] = 0
            dp[0][finger_pos][first_char] = 0
        for index in range(1, length):
            prev_char = ord(word[index - 1]) - ord('A')
            curr_char = ord(word[index]) - ord('A')
            move_cost = get_distance(prev_char, curr_char)
            for other_finger in range(26):
                dp[index][curr_char][other_finger] = min(dp[index][curr_char][other_finger], dp[index - 1][prev_char][other_finger] + move_cost)
                dp[index][other_finger][curr_char] = min(dp[index][other_finger][curr_char], dp[index - 1][other_finger][prev_char] + move_cost)
                if other_finger == prev_char:
                    for prev_other_finger in range(26):
                        switch_cost = get_distance(prev_other_finger, curr_char)
                        dp[index][curr_char][other_finger] = min(dp[index][curr_char][other_finger], dp[index - 1][prev_other_finger][prev_char] + switch_cost)
                        dp[index][other_finger][curr_char] = min(dp[index][other_finger][curr_char], dp[index - 1][prev_char][prev_other_finger] + switch_cost)
        last_char = ord(word[-1]) - ord('A')
        return min(min(dp[length - 1][last_char]), min(dp[length - 1][finger][last_char] for finger in range(26)))
