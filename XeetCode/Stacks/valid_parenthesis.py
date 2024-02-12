class Solution:
    def isValid(self, s: str) -> bool:
        hx = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        stack = []
        for i in s:
            if i in hx:
                print(i)
                if stack and stack[-1] == hx[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return stack == []


"""
logic:


make a stack

for every char in string : "{}" example

put it in stack

first pass:
[{]
next, if '}' in hashmap, and if '{' : whats in the hx map ( a match), we have a match and remove that '{' out
if not, that means the string itself started with a closing parenthesis hence return False


finally return true if stack is empty
"""
