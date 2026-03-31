class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True