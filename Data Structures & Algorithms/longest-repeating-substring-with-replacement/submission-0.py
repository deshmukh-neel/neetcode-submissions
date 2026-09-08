from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ABABBA
        l = r = res = 0
        mp = {}
    
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            while ((r - l) + 1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, (r - l + 1))
        return res





