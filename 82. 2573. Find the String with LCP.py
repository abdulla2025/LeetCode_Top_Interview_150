class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        length = len(lcp)
        result = [""] * length
        current_pos = 0
        for current_char in ascii_lowercase:
            while current_pos < length and result[current_pos]:
                current_pos += 1
            if current_pos == length:
                break
            for next_pos in range(current_pos, length):
                if lcp[current_pos][next_pos]:
                    result[next_pos] = current_char
        if "" in result:
            return ""
        for row in range(length - 1, -1, -1):
            for col in range(length - 1, -1, -1):
                if result[row] == result[col]:
                    if row == length - 1 or col == length - 1:
                        if lcp[row][col] != 1:
                            return ""
                    elif lcp[row][col] != lcp[row + 1][col + 1] + 1:
                        return ""
                elif lcp[row][col]:
                    return ""
        return "".join(result)
