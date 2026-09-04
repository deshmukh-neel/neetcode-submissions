class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x in s_dict:
                s_dict[x] += 1
            else:
               s_dict[x] = 1 
        for y in t:
            if y in t_dict:
                t_dict[y] += 1
            else:
               t_dict[y] = 1
        for z in s_dict:
            if z not in t_dict:
                return False
            if s_dict[z] != t_dict[z]: 
                return False
        return True 