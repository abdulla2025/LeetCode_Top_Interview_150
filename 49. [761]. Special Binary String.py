class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if s == '':
            return ''
        
        special_strings = []
        balance = 0
        start = current = 0
        
        while current < len(s):
            balance += 1 if s[current] == '1' else -1
            if balance == 0:
                inner = s[start + 1 : current]
                special_strings.append('1' + self.makeLargestSpecial(inner) + '0')
                start = current + 1
            current += 1
        
        special_strings.sort(reverse=True)
        return ''.join(special_strings)
