class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_size = len(s) 
        t_size = len(t) 
        s_dict = {}
        t_dict = {}

        if t_size != s_size: 
            return False 
        # check if they have same number of characters 
        for key in s: 
            if key in s_dict:
                s_dict[key] = s_dict[key] + 1 
            else: 
                s_dict[key] = 1 
        # now we have a full s_dict with frequency of 
        # each letter in s 
        for key in t: 
            if key in t_dict:
                t_dict[key] = t_dict[key] + 1 
            else: 
                t_dict[key] = 1 
        print(s_dict)
        print(t_dict)
        for key in s_dict: 
            if s_dict[key] != t_dict.get(key, 0): 
                return False 
        return True 
