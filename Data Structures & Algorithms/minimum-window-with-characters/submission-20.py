class Solution:
    def validWindow(self, arr, target) -> bool:
        for i in range(len(arr)):
            if arr[i] < target[i]:
                return False
        return True

    def letterToIndex(self, char):
        if char.isupper():
            return ord(char) - ord('A')
        if char.islower():
            return ord(char) - ord('A') - 6

    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        if len(t) > len(s):
            return ''
        
        # sliding window
        # width = starts at len(t)
        # if doesnt have all letters, expand right
        # once we have all letters, record in minLen
        # with minLen[0] = len, minLen[1-2] = indices
        # then we can shift left & keep recording
        # if still valid
        # if not valid, then go back to shifting right index
        # go until right > len(s)

        # for checking if window is valid (has all letters):
        # have a target array of size 52 (upper & lower)
        # and count each char
        # then have a running count of size 52
        # when this running count has every index
        # with a value >= to target
        # then we good!
        minLen = [len(s) + 1, -1, -1]
        
        target_counts = [0] * 52
        for c in t:
            target_counts[self.letterToIndex(c)] += 1
        
        l = 0
        r = len(t) - 1

        running_counts = [0] * 52
        for i in range(l, r):
            running_counts[self.letterToIndex(s[i])] += 1

        while l < len(s):
            if self.validWindow(running_counts, target_counts):
                if r - l < minLen[0]:
                    minLen = [r - l, l, r]
                running_counts[self.letterToIndex(s[l])] -= 1
                l += 1
            else:
                if r < len(s):
                    running_counts[self.letterToIndex(s[r])] += 1
                    r += 1
                else:
                    running_counts[self.letterToIndex(s[l])] -= 1
                    l += 1
        
        res = ""
        for i in range(minLen[1], minLen[2]):
            res += s[i]
        return res
