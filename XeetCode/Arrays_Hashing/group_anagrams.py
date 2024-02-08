class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master = []
        hx = set()
        for word in strs:
            s = "".join(sorted(word))
            if s not in hx:
                hx.add(s)
                master.append([word])
            else:
                for i in master:
                    if s == "".join(sorted(i[0])):
                        i.append(word)
        return master


"""
my first sol
runs in O(N)
"""

"""
second sol

"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hx = defaultdict(list)
        for word in strs:
            s = str(sorted(map(ord, word)))
            if s not in hx:
                hx[s].append(word)
            else:
                hx[s].append(word)
        return [x for x in hx.values()]


"""
SINCE SORTNG!
time: 
The overall time complexity is O(n * m * log(m)), where n is the number of words in strs, and m is the length of the longest word.
Time Complexity:

    The for loop iterates through each word in the input list strs. Let's denote the length of the longest word in strs as m.
    Inside the loop, there is a sorting operation on the characters of each word, and then a conversion to a string. The sorting operation has a time complexity of O(m*log(m)) in the worst case, where m is the length of the word.
    The map(ord, word) operation also takes O(m) time.
    The hx[s] dictionary access and append operation take constant time on average.
    The final list comprehension at the end takes O(n) time, where n is the number of unique anagram groups.


space: O(n)



WHAT I LEARNT:

!!! Tuples are hashable (WHY? CZ ITS IMUATABLE, ANYTHING THATS IMUTABLE CAN BE HASHED! (MADE KEY IN DICT)), and using them as keys in a dictionary can be more efficient than using lists. !!! 


DEFAULT DICT DOESN'T NEED EXPLICIT CHECK, IT DOES IT ON ITS OWN!


report: goood, built intuation on own (how can i transform the data into some sort way to hash it)

"""


# FASTEST

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hx = defaultdict(list)

        for word in strs:
            s = tuple(sorted(map(ord, word)))
            hx[s].append(word)

        return list(hx.values())
