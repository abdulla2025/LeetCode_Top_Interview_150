class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_chars_s1 = [s1[0], s1[2]]
        odd_chars_s1 = [s1[1], s1[3]]
        even_chars_s2 = [s2[0], s2[2]]
        odd_chars_s2 = [s2[1], s2[3]]

        even_chars_s1.sort()
        odd_chars_s1.sort()
        even_chars_s2.sort()
        odd_chars_s2.sort()

        if even_chars_s1 == even_chars_s2:
            if odd_chars_s1 == odd_chars_s2:
                return True
            else:
                return False
        else:
            return False
