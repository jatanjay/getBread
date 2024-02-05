# 1.0


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if set(t) == set(s):
                return True
        return False


"""
What was wrong:
wasn't clear on the edge case, set will take out all the letters out


To Learn:
Early return has to be added, i did notice the importnace of length, should add that ground condition asap


"""

# 2.0


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)):
            return True
        return False


"""
space: O(n)
time: O(n)


How did you improve
idea was:

how can length of 2 words be taken into account
how to weed out repitative characters (where set fails)
hence did sorted(list)

but ineff

"""
# 3.0


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        g, f = dict(), dict()
        for x in s:
            if x not in g:
                g[x] = 1
            else:
                g[x] += 1

        for x in t:
            if x not in f:
                f[x] = 1
            else:
                f[x] += 1

        if g == f:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True


"""
space: O(n)
time: O(n)

How did you improve:

thought about hash map, hence dictonary
my approach: good, but looks naive
is repitative:

Second solution is much more effiecnt:

1. uses get method
2. only creates one hashmap, and then uses other to makes sense out of it

 for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

Explained::
since the .get function above, sets the default value at 0, we need to check if there are no zeros, hence
we decrement by one each time it reaches 0



what i learn;
use get function for efficent
try not to reuse same type of logic twice

"""

# 4


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


"""
flexing, doesn't show lot of software accumen, just quick and dirty way
"""
