class Solution:
    def minOperations(self, s: str, k: int) -> int:
        str_len = len(s)
        parity_sets = [SortedSet() for _ in range(2)]
        for i in range(str_len + 1):
            parity_sets[i % 2].add(i)
        zero_count = s.count('0')
        parity_sets[zero_count % 2].remove(zero_count)
        bfs_queue = deque([zero_count])
        min_ops = 0
        while bfs_queue:
            for _ in range(len(bfs_queue)):
                cur_zeros = bfs_queue.popleft()
                if cur_zeros == 0:
                    return min_ops
                min_reachable = cur_zeros + k - 2 * min(cur_zeros, k)
                max_reachable = cur_zeros + k - 2 * max(k - str_len + cur_zeros, 0)
                same_parity_set = parity_sets[min_reachable % 2]
                idx = same_parity_set.bisect_left(min_reachable)
                while idx < len(same_parity_set) and same_parity_set[idx] <= max_reachable:
                    next_zeros = same_parity_set[idx]
                    bfs_queue.append(next_zeros)
                    same_parity_set.remove(next_zeros)
            min_ops += 1
        return -1
