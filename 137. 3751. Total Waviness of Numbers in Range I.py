class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x):
            s=str(x)
            if len(s)<3:
                return 0
            cnt=0
            for i in range(1,len(s)-1):
                if s[i]>s[i-1] and s[i]>s[i+1]:
                    cnt+=1
                elif s[i]<s[i-1] and s[i]<s[i+1]:
                    cnt+=1
            return cnt
        total=0
        for num in range(num1,num2+1):
            total+=waviness(num)
        return total