class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        opens = "({["
        closes = ")}]"

        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in opens:
                stack.append(c)
            
            if c in closes:
                if len(stack) == 0:
                    return False
                if closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0