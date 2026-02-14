class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curr = [poured]
        for row in range(query_row):
            nxt = [0] * (row + 2)
            for col in range(len(curr)):
                if curr[col] > 1:
                    overflow = (curr[col] - 1) / 2
                    nxt[col] += overflow
                    nxt[col + 1] += overflow
            curr = nxt
        return min(1, curr[query_glass])
