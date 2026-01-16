class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        h_positions = [1] + sorted(hFences) + [m]
        v_positions = [1] + sorted(vFences) + [n]
        horizontal_dists = set()
        for i in range(len(h_positions)):
            for j in range(i + 1, len(h_positions)):
                horizontal_dists.add(h_positions[j] - h_positions[i])
        
        vertical_dists = set()
        for i in range(len(v_positions)):
            for j in range(i + 1, len(v_positions)):
                vertical_dists.add(v_positions[j] - v_positions[i])
        
        max_common = 0
        for dist in horizontal_dists:
            if dist in vertical_dists:
                max_common = max(max_common, dist)
        
        if max_common == 0:
            return -1
        
        return (max_common * max_common) % MOD