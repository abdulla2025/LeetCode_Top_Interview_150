class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_gap = 0
        last_one = -1
        
        for i, bit in enumerate(binary):
            if bit == '1':
                if last_one != -1:
                    gap = i - last_one
                    if gap > max_gap:
                        max_gap = gap
                last_one = i
        
        return max_gap
