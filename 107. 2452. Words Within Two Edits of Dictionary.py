class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        n = len(queries[0]) if queries else 0
        for q in queries:
            for d in dictionary:
                diff = 0
                for i in range(n):
                    if q[i] != d[i]:
                        diff += 1
                        if diff > 2:
                            break
                if diff <= 2:
                    result.append(q)
                    break
        return result
