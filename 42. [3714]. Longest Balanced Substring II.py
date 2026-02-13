class Solution:
    def longestBalanced(self, s: str) -> int:
        def f1(t: str) -> int:
            r = 0
            i, m = 0, len(t)
            while i < m:
                j = i + 1
                while j < m and t[j] == t[i]:
                    j += 1
                r = max(r, j - i)
                i = j
            return r
        def f2(t: str, x: str, y: str) -> int:
            r = 0
            i, m = 0, len(t)
            while i < m:
                while i < m and t[i] not in (x, y):
                    i += 1
                p = {0: i - 1}
                d = 0
                while i < m and t[i] in (x, y):
                    d += 1 if t[i] == x else -1
                    if d in p:
                        r = max(r, i - p[d])
                    else:
                        p[d] = i
                    i += 1
            return r
        def f3(t: str) -> int:
            p = {(0, 0): -1}
            c = Counter()
            r = 0
            for i, ch in enumerate(t):
                c[ch] += 1
                k = (c["a"] - c["b"], c["b"] - c["c"])
                if k in p:
                    r = max(r, i - p[k])
                else:
                    p[k] = i
            return r
        return max(f1(s), max(f2(s, "a", "b"), f2(s, "b", "c"), f2(s, "a", "c")), f3(s))
