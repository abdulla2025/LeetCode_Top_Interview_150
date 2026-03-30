class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1 = []
        even2 = []
        odd1 = []
        odd2 = []
        for i in range(len(s1)):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])
            else:
                odd1.append(s1[i])
                odd2.append(s2[i])
        even1.sort()
        even2.sort()
        odd1.sort()
        odd2.sort()
        if even1 == even2 and odd1 == odd2:
            return True
        else:
            return False
