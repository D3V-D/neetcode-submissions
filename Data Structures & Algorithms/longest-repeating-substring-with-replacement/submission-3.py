class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # keep increasing as long as there is at most k chars.
        # that are not in the longest consecutive
        # if more than k, store previous length if max
        # and increase left until <= k
        # then we can again try icrememting r

        # how to check if >k other letters:
        # keep track of historical max
        # with map
        freqs = {}
        maxf = 0
        maxLen = 0
        l = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxf = max(maxf, freqs[s[r]])
            while (r - l + 1) - maxf > k:
                freqs[s[l]] = freqs[s[l]] - 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
   
