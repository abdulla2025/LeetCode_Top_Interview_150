class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * n
        seenA = set()
        seenB = set()
        count = 0
        
        for i in range(n):
            if A[i] in seenB:
                count += 1
            seenA.add(A[i])
            
            if B[i] in seenA:
                count += 1
            seenB.add(B[i])
            
            res[i] = count
        
        return res
