from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key=lambda x: x[1])
        
        n = len(squares)
        bottoms = [s[1] for s in squares]
        tops = [s[1] + s[2] for s in squares]
        lengths = [s[2] for s in squares]
        areas = [l * l for l in lengths]
        
        min_y = min(bottoms)
        max_y = max(tops)
        def area_below(y):
            total = 0.0
            for i in range(n):
                bottom = bottoms[i]
                top = tops[i]
                l = lengths[i]
                
                if y <= bottom:
                    continue
                elif y >= top:
                    total += l * l
                else:
                    total += l * (y - bottom)
            return total
        
        target = sum(areas) / 2.0
        left, right = min_y, max_y
        
        for _ in range(100): 
            mid = (left + right) / 2
            below = area_below(mid)
            
            if below < target:
                left = mid
            else:
                right = mid
        
        return left