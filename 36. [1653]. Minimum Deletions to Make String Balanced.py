class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        for char in s:
            if char == 'b':
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)
        return deletions
