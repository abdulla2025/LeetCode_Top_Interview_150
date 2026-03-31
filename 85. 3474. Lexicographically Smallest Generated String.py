class Solution:
    def generateString(self, pattern: str, target: str) -> str:
        n,m=len(pattern),len(target)
        result=["a"]*(n+m-1)
        is_fixed=[False]*(n+m-1)
        for i,ch in enumerate(pattern):
            if ch!="T":
                continue
            for j,t_char in enumerate(target):
                pos=i+j
                if is_fixed[pos] and result[pos]!=t_char:
                    return ""
                result[pos]=t_char
                is_fixed[pos]=True
        for i,ch in enumerate(pattern):
            if ch!="F":
                continue
            if "".join(result[i:i+m])!=target:
                continue
            for j in range(i+m-1,i-1,-1):
                if not is_fixed[j]:
                    result[j]="b"
                    break
            else:
                return ""
        return "".join(result)
