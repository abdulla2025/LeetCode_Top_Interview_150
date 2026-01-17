class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                a1, b1 = bottomLeft[i]
                c1, d1 = topRight[i]
                a2, b2 = bottomLeft[j]
                c2, d2 = topRight[j]
                intersect_bl_x = max(a1, a2)
                intersect_bl_y = max(b1, b2)
                intersect_tr_x = min(c1, c2)
                intersect_tr_y = min(d1, d2)
                width = intersect_tr_x - intersect_bl_x
                height = intersect_tr_y - intersect_bl_y
                
                if width > 0 and height > 0:
                    side_length = min(width, height)
                    area = side_length * side_length
                    max_area = max(max_area, area)
        
        return max_area