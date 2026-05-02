class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = {'3', '4', '7'}
        changing = {'2', '5', '6', '9'}

        count = 0
        for x in range(1, n + 1):
            s = str(x)
            has_change = False
            valid = True
            for ch in s:
                if ch in invalid:
                    valid = False
                    break
                if ch in changing:
                    has_change = True
            if valid and has_change:
                count += 1
        return count
