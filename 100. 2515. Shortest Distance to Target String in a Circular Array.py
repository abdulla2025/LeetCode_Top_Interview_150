class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')

        for i in range(n):
            if words[i] == target:
                diff = abs(i - startIndex)
                distance = min(diff, n - diff)
                min_dist = min(min_dist, distance)

        if min_dist == float('inf'):
            return -1
        return min_dist