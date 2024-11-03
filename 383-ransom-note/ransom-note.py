class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False
        mag = Counter(magazine)
        ran = Counter(ransomNote)
        for keys in ran:
            if keys in mag and mag[keys] >= ran[keys]:
                continue 
            else:
                return False
        return True 