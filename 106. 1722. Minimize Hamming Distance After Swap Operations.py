class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        n = len(source)
        parent = list(range(n))
        for a,b in allowedSwaps:
            parent[find(a)] = find(b)
        
        groups = {}
        for i,val in enumerate(source):
            root = find(i)
            if root not in groups:
                groups[root] = {}
            groups[root][val] = groups[root].get(val,0) + 1
        
        ans = 0
        for i,val in enumerate(target):
            root = find(i)
            if groups[root].get(val,0) > 0:
                groups[root][val] -= 1
            else:
                ans += 1
        return ans
