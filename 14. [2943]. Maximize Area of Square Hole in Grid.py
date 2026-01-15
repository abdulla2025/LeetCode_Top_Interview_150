class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def findMaxConsecutive(bars):
            if not bars:
                return 1
            
            bars.sort()
            max_length = 1
            current_length = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    current_length = 1

            return max_length + 1
        
        max_h_gap = findMaxConsecutive(hBars)
        max_v_gap = findMaxConsecutive(vBars)
        
        side = min(max_h_gap, max_v_gap)
        
        return side * side