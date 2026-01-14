class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        class SegmentTree:
            def __init__(self, sorted_x):
                self.sorted_x = sorted_x
                n = len(sorted_x) - 1
                size = 1 << ((n - 1).bit_length() + 1)
                self.tree = [0] * size
                self.cnt = [0] * size
            
            def update(self, ql, qr, delta, l=0, r=None, idx=1):
                if r is None:
                    r = len(self.sorted_x) - 1
                
                if ql >= r or qr <= l:
                    return
                
                if ql <= l and r <= qr:
                    self.cnt[idx] += delta
                else:
                    mid = (l + r) // 2
                    self.update(ql, qr, delta, l, mid, 2 * idx)
                    self.update(ql, qr, delta, mid, r, 2 * idx + 1)
                
                if self.cnt[idx] > 0:
                    self.tree[idx] = self.sorted_x[r] - self.sorted_x[l]
                else:
                    if r - l == 1:
                        self.tree[idx] = 0
                    else:
                        self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]
        
        events = []
        x_coords = set()
        
        for x, y, length in squares:
            events.append((y, 1, x, x + length))
            events.append((y + length, -1, x, x + length))
            x_coords.add(x)
            x_coords.add(x + length)
        
        events.sort()
        
        sorted_x = sorted(x_coords)
        x_to_idx = {x: i for i, x in enumerate(sorted_x)}
        
        seg_tree = SegmentTree(sorted_x)
        prev_y = events[0][0]
        intervals = []
        
        for y, delta, x1, x2 in events:
            if y != prev_y:
                intervals.append((prev_y, y, seg_tree.tree[1]))
                prev_y = y
            seg_tree.update(x_to_idx[x1], x_to_idx[x2], delta)
        
        total_area = sum((y2 - y1) * width for y1, y2, width in intervals)
        target_area = total_area / 2.0
        
        cumulative_area = 0.0
        for y1, y2, width in intervals:
            if cumulative_area + (y2 - y1) * width >= target_area:
                remaining = target_area - cumulative_area
                return y1 + remaining / width
            cumulative_area += (y2 - y1) * width
        
        return intervals[-1][1]