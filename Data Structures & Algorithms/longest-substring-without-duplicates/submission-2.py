class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        maxLen = 0

        while l < len(s) and r < len(s):
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                r += 1
                print(seen)
                maxLen = max(len(seen), maxLen)
            while r < len(s) and s[r] in seen:
                seen.remove(s[l])
                l += 1
                if l > len(s) - 1:
                    break
        return maxLen