class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for lett in s: 
            s_dict[lett] = 1+s_dict.get(lett, 0)
        for lett in t:
            t_dict[lett] = 1+t_dict.get(lett,0)
        if t_dict == s_dict:
            return True
        return False
