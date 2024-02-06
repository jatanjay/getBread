import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[\W_]", "", s).lower()
        return s == s[::-1]


"""
took the longest time to understand the regex
was on right path, needed brushing of regex concept
"""
