from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hx = Counter(nums)
        s = sorted([(v, k) for k, v in hx.items()], key=lambda x: x[0], reverse=True)
        f = []
        for i in range(len(s[:k])):
            f.append(s[i][1])
        return f


"""
my sol: 
seems kinda brute force? def in o log n
did some patch work in doing sorting
"""


# need to understand better ans : #TODO
