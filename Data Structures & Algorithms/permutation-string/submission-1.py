class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        targets = {}

        for c in s1:
            targets[c] = targets.get(c, 0) + 1
        
        # window of size len(s1)
        l = 0
        r = len(s1) - 1

        # each char in window must be in set, otherwise cont.
        while r < len(s2):
            tt = targets.copy()
            for i in range(l, r + 1):
                if s2[i] in tt:
                    tt[s2[i]] -= 1
                    if tt[s2[i]] == 0:
                        tt.pop(s2[i])
                        print(s2[i])
                        print("POP")
                    if not tt:
                        return True
            r += 1
            l += 1

        return False