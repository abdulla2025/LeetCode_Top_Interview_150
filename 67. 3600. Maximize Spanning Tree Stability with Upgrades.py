class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        if self.size[root1] > self.size[root2]:
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
        else:
            self.parent[root1] = root2
            self.size[root2] += self.size[root1]
        self.components -= 1
        return True

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def can_connect_all(min_strength: int) -> bool:
            uf = UnionFind(n)
            for node1, node2, strength, _ in edges:
                if strength >= min_strength:
                    uf.union(node1, node2)
            optional_swaps_left = k
            for node1, node2, strength, _ in edges:
                if strength * 2 >= min_strength and optional_swaps_left > 0:
                    if uf.union(node1, node2):
                        optional_swaps_left -= 1
            return uf.components == 1

        uf = UnionFind(n)
        min_mandatory_strength = 10**6
        for node1, node2, strength, is_mandatory in edges:
            if is_mandatory:
                min_mandatory_strength = min(min_mandatory_strength, strength)
                if not uf.union(node1, node2):
                    return -1
        for node1, node2, _, _ in edges:
            uf.union(node1, node2)
        if uf.components > 1:
            return -1

        low, high = 1, min_mandatory_strength
        while low < high:
            mid = (low + high + 1) >> 1
            if can_connect_all(mid):
                low = mid
            else:
                high = mid - 1
        return low
