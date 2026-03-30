class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        map1 = {}
        map2 = {}

        for i in range(len(s)):
            map1[s[i]] = map1[s[i]] + 1 if s[i] in map1 else 1;
            map2[t[i]] = map2[t[i]] + 1 if t[i] in map2 else 1;
        
        for c in map1:
            if c not in map2 or map2[c] != map1[c]:
                return False
        return True
        
        
