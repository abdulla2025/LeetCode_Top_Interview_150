class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bits = n.bit_length()
        mask = (1 << bits) - 1
        return n ^ mask
