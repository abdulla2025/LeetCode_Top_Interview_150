class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        perimeter_positions = []
        for x, y in points:
            if x == 0:  # left edge
                perimeter_positions.append(y)
            elif y == side:  # top edge
                perimeter_positions.append(side + x)
            elif x == side:  # right edge
                perimeter_positions.append(3 * side - y)
            else:  # bottom edge
                perimeter_positions.append(4 * side - x)

        perimeter_positions.sort()
        def can_pick(min_dist: int) -> bool:
            total_perimeter = 4 * side

            for start_idx in perimeter_positions:
                max_allowed = start_idx + total_perimeter - min_dist
                current = start_idx

                valid = True

                for _ in range(k - 1):
                    next_idx = bisect_left(perimeter_positions, current + min_dist)

                    if next_idx == len(perimeter_positions) or perimeter_positions[next_idx] > max_allowed:
                        valid = False
                        break

                    current = perimeter_positions[next_idx]

                if valid:
                    return True

            return False
        left, right = 1, side
        while left < right:
            mid_dist = (left + right + 1) // 2
            if can_pick(mid_dist):
                left = mid_dist
            else:
                right = mid_dist - 1
        return left
