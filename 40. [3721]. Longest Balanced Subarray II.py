class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        size = len(nums)
        class SegNode:
            __slots__ = ("left", "right", "min_val", "max_val", "delta")
            def __init__(self):
                self.left = self.right = 0
                self.min_val = self.max_val = 0
                self.delta = 0
        tree = [SegNode() for _ in range((size + 1) * 4)]
        def construct(idx: int, lo: int, hi: int):
            tree[idx].left, tree[idx].right = lo, hi
            tree[idx].min_val = tree[idx].max_val = tree[idx].delta = 0
            if lo == hi:
                return
            mid = (lo + hi) >> 1
            construct(idx << 1, lo, mid)
            construct(idx << 1 | 1, mid + 1, hi)
        def update_node(idx: int, val: int):
            tree[idx].min_val += val
            tree[idx].max_val += val
            tree[idx].delta += val
        def propagate(idx: int):
            if tree[idx].delta:
                update_node(idx << 1, tree[idx].delta)
                update_node(idx << 1 | 1, tree[idx].delta)
                tree[idx].delta = 0
        def merge(idx: int):
            tree[idx].min_val = min(tree[idx << 1].min_val, tree[idx << 1 | 1].min_val)
            tree[idx].max_val = max(tree[idx << 1].max_val, tree[idx << 1 | 1].max_val)
        def range_update(idx: int, lo: int, hi: int, val: int):
            if tree[idx].left >= lo and tree[idx].right <= hi:
                update_node(idx, val)
                return
            propagate(idx)
            mid = (tree[idx].left + tree[idx].right) >> 1
            if lo <= mid:
                range_update(idx << 1, lo, hi, val)
            if hi > mid:
                range_update(idx << 1 | 1, lo, hi, val)
            merge(idx)
        def find_pos(idx: int, target: int) -> int:
            if tree[idx].left == tree[idx].right:
                return tree[idx].left
            propagate(idx)
            if tree[idx << 1].min_val <= target <= tree[idx << 1].max_val:
                return find_pos(idx << 1, target)
            return find_pos(idx << 1 | 1, target)
        construct(1, 0, size)
        prev_pos = {}
        balance = result = 0
        for pos, num in enumerate(nums, start=1):
            diff = 1 if (num & 1) else -1
            if num in prev_pos:
                range_update(1, prev_pos[num], size, -diff)
                balance -= diff
            prev_pos[num] = pos
            range_update(1, pos, size, diff)
            balance += diff
            loc = find_pos(1, balance)
            result = max(result, pos - loc)
        return result
