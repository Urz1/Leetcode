class Solution(object):
    def isIsomorphic(self, s, t):
        s_to_t_map = {}
        t_to_s_map = {}
        
        for s_char, t_char in zip(s, t):
            if (s_char in s_to_t_map and s_to_t_map[s_char] != t_char) or \
                (t_char in t_to_s_map and t_to_s_map[t_char] != s_char):
                return False
            
            s_to_t_map[s_char] = t_char
            t_to_s_map[t_char] = s_char
        
        return True
        