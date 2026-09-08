class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        res1 = [0] * 26
        for c in s1:
            res1[ord(c) - ord('a')] += 1
        l = 0
        for r in range((n1 - 1), n2, 1):
            # abc
            # lecabee
            res2 = [0] * 26
            i = l
            while i <= r:
                res2[ord(s2[i]) - ord('a')] += 1
                i += 1
            l += 1
            if res1 == res2:
                return True
        return False